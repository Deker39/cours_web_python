String.prototype.firstLetterCaps = function () {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

function creatInputElement(key, value) {
    return $(
        '<div class="row align-items-center py-1">' +
        ' <div class="col-sm-6">' +
        `<label for="input${key}" class="col-form-label">${key.firstLetterCaps()}: </label>` +
        '</div>' +
        '<div class="col-sm-6">' +
        `<input type="text" id="input${key}" class="form-control" name="${key}" value="${value}">` +
        '</div>' +
        '</div>'
    )

}

function edit_element(id) {
    console.log(`edit ${id}`)
    console.log($(`#id${id}`))
    fetch(`http://127.0.0.1:5000/edit/${id}`)
        .then(data => {
            data.json().then(e => {
                console.log(Object.entries(e))
                let saveFrom = $('<form class="m-2" method="POST"></form>')
                for (const [key, value] of Object.entries(e)) {
                    let elem = creatInputElement(key, value)
                    saveFrom.append(elem)
                }
                $(`#id${id}`).parent().append(saveFrom.append($('' +
                    '<div class="row align-items-center py-1">' +
                    ' <div class="col-sm-12">' +
                    `<button type="submit" class="btn btn-secondary" style="width:100%;" name="submit">Submit</button>` +
                    '</div>' +
                    '</div>')))
                $(`#id${id}`).toggle()

            }

            )
        })
}


function delete_element(id) {
    console.log(`edit ${id}`)
    fetch(`http://127.0.0.1:5000/delete/${id}`)
        .then(data => {
            data.json().then(e => {
                console.log(e)
                if (e['answer'] === 'delete') {
                    location.reload();
                }
                else {
                    console.log('error delete')
                }
            })
        })

}