document.addEventListener("DOMContentLoaded", function () {

    const ATTRIBUTE_SELECT = 'select[name$="-attribute"]';
    const VALUE_SELECT = 'select[name$="-attribute_value"]';
    const PREFIX = "productattributevalue_set";

    function getRow(el) {
        return (
            el.closest(".form-row") ||
            el.closest(".inline-related") ||
            el.closest("tr")
        );
    }

    // ---- Attribute -> Value cascade ----
    function loadAttributeValues(attributeSelect, preselectValue) {
        const row = getRow(attributeSelect);
        const valueSelect = row ? row.querySelector(VALUE_SELECT) : null;
        if (!valueSelect) return;

        const attributeId = attributeSelect.value;
        const currentValue =
            preselectValue !== undefined ? preselectValue : valueSelect.value;

        if (!attributeId) {
            valueSelect.innerHTML = '<option value="">---------</option>';
            return;
        }

        fetch(`/products/get-attribute-values/?attribute_id=${attributeId}`)
            .then((response) => response.json())
            .then((data) => {
                valueSelect.innerHTML = '<option value="">---------</option>';

                data.forEach(function (value) {
                    const option = document.createElement("option");
                    option.value = value.id;
                    option.textContent = value.attribute_value;
                    valueSelect.appendChild(option);
                });

                if (currentValue) {
                    valueSelect.value = currentValue;
                }
            });
    }

    // ---- Fix an attribute select to a single known attribute ----
    // Keeps it a real <select> (so it still submits) but removes the
    // ability to pick a different attribute for this row.
    function lockAttributeSelect(attributeSelect, attributeId, attributeName) {
        attributeSelect.innerHTML = "";
        const option = document.createElement("option");
        option.value = attributeId;
        option.textContent = attributeName;
        option.selected = true;
        attributeSelect.appendChild(option);
    }

    // ---- Add a new inline row for a given attribute ----
    function addAttributeRow(attributeId, attributeName) {
        const totalFormsInput = document.querySelector(
            `input[name="${PREFIX}-TOTAL_FORMS"]`
        );
        const emptyRow = document.querySelector(
            `#${PREFIX}-empty, tr.empty-form, div.empty-form`
        );

        if (!totalFormsInput || !emptyRow) return;

        const formIndex = parseInt(totalFormsInput.value, 10);

        const newRow = emptyRow.cloneNode(true);
        newRow.classList.remove("empty-form");
        newRow.removeAttribute("id");
        newRow.innerHTML = newRow.innerHTML.replace(/__prefix__/g, formIndex);
        newRow.style.display = "";

        emptyRow.parentNode.insertBefore(newRow, emptyRow);
        totalFormsInput.value = formIndex + 1;

        const attributeSelect = newRow.querySelector(ATTRIBUTE_SELECT);
        if (!attributeSelect) return;

        lockAttributeSelect(attributeSelect, attributeId, attributeName);
        loadAttributeValues(attributeSelect, "");
    }

    // ---- Add rows for any attribute belonging to the product type ----
    // that doesn't already have a row on the page ----
    function syncAttributeRows(productTypeId) {
        if (!productTypeId) return;

        fetch(`/products/get-attributes/?product_type_id=${productTypeId}`)
            .then((response) => response.json())
            .then((attributes) => {
                const existingIds = new Set();

                document.querySelectorAll(ATTRIBUTE_SELECT).forEach(function (select) {
                    if (select.closest(".empty-form")) return;
                    if (select.value) existingIds.add(String(select.value));
                });

                attributes.forEach(function (attribute) {
                    if (!existingIds.has(String(attribute.id))) {
                        addAttributeRow(attribute.id, attribute.attribute);
                    }
                });
            });
    }

    // ---- Init: lock existing rows down + preload their value dropdown ----
    document.querySelectorAll(ATTRIBUTE_SELECT).forEach(function (attributeSelect) {
        if (attributeSelect.closest(".empty-form")) return;

        const selectedOption = attributeSelect.options[attributeSelect.selectedIndex];
        if (selectedOption && selectedOption.value) {
            lockAttributeSelect(
                attributeSelect,
                selectedOption.value,
                selectedOption.textContent
            );
        }
        loadAttributeValues(attributeSelect);
    });

    // ---- product_type -> attribute rows ----
    const productTypeSelect = document.getElementById("id_product_type");
    if (productTypeSelect) {
        if (productTypeSelect.value) {
            syncAttributeRows(productTypeSelect.value);
        }
        productTypeSelect.addEventListener("change", function () {
            syncAttributeRows(this.value);
        });
    }

    // ---- attribute change -> reload value dropdown (existing rows only) ----
    document.addEventListener("change", function (event) {
        if (event.target.matches(ATTRIBUTE_SELECT)) {
            loadAttributeValues(event.target);
        }
    });
});