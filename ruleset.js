const input = document.getElementById("quantity");
const container = document.getElementById("rules");

input.addEventListener("input", generateBoxes);

function generateBoxes(){
    const count = parseInt(input.value) || 2;
    if(count < 2 || count > 5){
        count = 2;
    }
    container.innerHTML = "";

    for(let i = 0; i < count; i++){
        const wrapper = document.createElement("div");
        const wrapper2 = document.createElement("span");

        const label = document.createElement("label");
        label.setAttribute("for", "relation" + i);
        label.textContent = "Case x % " + count + " = " + i;
        
        const field = document.createElement("input");
        field.type = "text";
        field.id = "relation" + i;
        field.name = "relation";
        field.className = "relation";
        if(i === 0){
            field.placeholder = "x / " + count;
        }
        else{
            field.placeholder = "x + 1";
        }
        field.required = true;

        wrapper2.appendChild(label);
        wrapper2.appendChild(field);
        wrapper.appendChild(wrapper2);
        container.appendChild(wrapper);
    }
}

generateBoxes();