async function getItems() {
    return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
}

async function refreshItems() {
    document.getElementById("item_view").innerHTML = ""
    const items = await getItems()
    let htmlString = ``
    items.forEach((item) => {
        htmlString += `<div class="container">
        <div class="row" style="margin-top: 109px;">
            <div class="col-md-6">
                <img src="${ item.fields.image }">
            </div>
            <div class="col-md-6">
                <div class="card" style="margin-top: 38px;" id="inventorys">
                    <div class="card-body">
                        <h4 class="card-title">${ item.fields.name }</h4>
                    <p class="card-text">${ item.fields.description }</p>
                        <div>
                            <p class="fx-bold mb-0">Jumlah Tersimpan : ${ item.fields.amount }</p>
                            <p class="text-muted mb-0">Tipe Engine : ${ item.fields.engine }</p>
                            <p class="text-muted mb-0">Winglet : ${ item.fields.winglet }</p>
                            <div class="dropdown" id="button_dropdown" style="margin-top: 6px">
                                <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                                    Action
                                </button>
                                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a class="dropdown-item" href="{% url 'main:add_amount' item.id %}">Add Amount</a></li>
                                    <li><a class="dropdown-item" href="{% url 'main:sub_amount' item.id %}">Sub Amount</a></li>
                                    <li><a class="dropdown-item" href="{% url 'main:delete_data' item.id %}">Delete Data</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`
    })

    document.getElementById("item_view").innerHTML = htmlString
}

function addProduct() {
    fetch("{% url 'main:add_item_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}


refreshItems()