// CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const csrftoken = getCookie('csrftoken');
const defaultHeaders = {"X-CSRFToken": csrftoken};

function ajaxCall(url, method = 'GET', data = {}, headers = defaultHeaders) {
    return $.ajax({
        url: url,
        headers: headers,
        data: data,
        method: method,
        dataType: 'json',
        success: (result) => {
            console.log(result);
        },
        error: function(xhr, status, error) {
            console.log(xhr.responseText);
        }
    });
}


const eventsBlock = $("#events-block");

function cancelRegistration(data) {
    console.log(data);
    ajaxCall("/api/event/cancel/", "POST", data).then(() => {
        location.reload();
    });
}

function addRegistration(data, codeBlock, btn) {
    console.log(data);
    ajaxCall("/api/event/register/", "POST", data).then((res) => {
        const block = $(`<p>Your code is: <b>${res.code}</b></p>`);
        codeBlock.append(block);
        btn.prop("disabled", true);
    });
}

function setEvents(events) {
    events.forEach(event => {
        const startAt = new Date(event.start_at);
        const endAt = new Date(event.end_at);
        const signleEvent = $(`
            <div class="single-event default-block">
                <p>Title: ${event.title}</p>
                <p>Starts at: ${startAt}</p>
                <p>Ends at: ${endAt}</p>
            </div>
        `);

        // Attend btn
        if (!event.is_user) {
            const attendButton = $(`
                <button class="btn btn-primary">Attend</button>
            `);
            attendButton.click(() => {addRegistration({event_id: event.id}, signleEvent, attendButton)});
            signleEvent.append(attendButton);
        }
        // Cancel btn
        if (event.is_user) {
            const inputField = $(`
                <input type="text" class="form-control" placeholder="Enter code" maxlength="16">
            `);
            const cancelButton = $(`
                <button class="btn btn-danger">Cancel</button>
            `);
            cancelButton.click(() => {cancelRegistration(
                {code: inputField.val(), can_be_cancelled: event.can_be_cancelled}
            )});
            if (!event.can_be_cancelled) {
                cancelButton.prop("disabled", true);
                inputField.prop("disabled", true);
            }
            signleEvent.append(cancelButton);
            signleEvent.append(inputField);
        }

        eventsBlock.append(signleEvent);
    });
}


$(window).on('load', async () => {
    const events = await ajaxCall("/api/event/fetch-all");
    setEvents(events);
});
