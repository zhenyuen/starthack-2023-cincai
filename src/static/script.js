'use strict';


window.addEventListener('load', async function () {
    const session_id = prompt("Please input session id: ")
    const chat = await get_chat(session_id)
    const users = await get_users(session_id)
    const mlfs = await get_mlfs(session_id)
    const mlcluster = await get_mlcluster(mlfs)

    const messages = chat.messages
    const risks = chat.risks
    const timestamps = chat.timestamp
    const formatted = messages.map(function(e) { 
        return `${e.username}: ${e.message}`;
    });
    // console.log(users)
    const summary = await get_summary(formatted, users)
    const summary_e = document.getElementById("summary-text");
    summary_e.textContent = summary

    const node = document.getElementById("chat-li");

    for (let i = 0; i < messages.length; i++) {
        const e = messages[i]
        const t = timestamps[i]
        const c0 = document.createElement("li")
        const c1 = document.createElement("div")
        c1.className = "chat-container"
        const c2 = document.createElement("div")
        c2.className = "text-corrector"
        const c3 = this.document.createElement("p")
        c3.className = "text"
        c3.textContent = `${e.username}: ${e.message}`
        const c4 = this.document.createElement("div")
        c4.className = "chat-time"
        const c5 = this.document.createElement("span")
        c5.setAttribute("style", "visibility: hidden")
        c5.textContent = risks[i]
        c4.textContent = t
        c2.appendChild(c3)
        c1.appendChild(c2)
        c1.appendChild(c4)
        c1.appendChild(c5)
        c0.appendChild(c1)
        node.appendChild(c0)
    }

    const node2 = document.getElementById("people");

    for (let i = 0; i < users.length; i++) {
        const c6 = this.document.createElement("div")
        c6.classList.add("tooltiptext")

        const metrics = ["Rating"]

        for (let i = 0; i < metrics.length; i++) {
            const c11 = this.document.createElement("p")
            c11.textContent = metrics[i]
            c6.appendChild(c11)
        } // Not sure if work

        const c0 = document.createElement("li")
        const c1 = document.createElement("div")
        c1.classList.add("player-container")
        c1.classList.add("tooltip")

        const c2 = document.createElement("span")
        c2.className = "player"
        c2.textContent = users[i].username
        const c3 = this.document.createElement("select")
        c3.className = "actions"
        const c41 = this.document.createElement("option")
        c41.value = ""
        c41.setAttribute("type", "disabled")
        c41.setAttribute("type", "selected")
        c41.setAttribute("type", "hidden")
        c41.textContent = "..."
        c3.appendChild(c41)

        let actions = ["Spamming", "Political", "Unintended", "Aggravation", "Abuse of play", "Harassment", "Hate", "Sexual", "Ignore"]
        let tags = ["permanent-ban", "temporary-ban", "unintended", "aggravation", "aop", "harassment", "hate", "sexual", "ignore"]

        for (let i = 0; i < actions.length; i++) {
            const c00 = this.document.createElement("option")
            c00.value = tags[i]
            c00.textContent = actions[i]
            c3.appendChild(c00)
        }
        c1.appendChild(c2)
        c1.appendChild(c3)
        c1.appendChild(c6)
        c0.appendChild(c1)
        node2.appendChild(c0)


        // c2.addEventListener("mouseover", function(event) {
        //     // Show the tooltip
        //     c1.style.display = "block";
        // });

        // c2.addEventListener("mouseout", function() {
        //     // Hide the tooltip
        //     c1.style.display = "none";
        // });

    }

    const chat_messages = document.getElementsByClassName("chat-container");

    for (let i = 0; i < chat_messages.length; i++) {
        var current = chat_messages[i]; // replace "myDiv" with the ID of your div
        var value = Number(chat_messages[i].lastElementChild.innerHTML)
        value = (value + 2) / 0.9
        var g = 255 - (value - 1) * 25.5; // decrease red value as value increases
        var r = (value - 1) * 25.5; // increase green value as value increases
        var b = 0; // set blue value to 0
        current.style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")";
    }


    const score_e = document.getElementById("score-value")
    score_e.textContent = `${mlcluster.cluster.slice(2,5)} out of 1.0`

    const descrip_e = document.getElementById("comment")
    descrip_e.textContent = `confidence score in chat containing inappropriate behaviour.`

});

async function get_chat(session_id) {
    return await fetch(`http://127.0.0.1:8080/chat?session_id=${session_id}`)
    .then((res) => {
        return res.json()
    })
    .then((obj) => {
        return obj
    })
}


async function get_mlfs(session_id) {
    return await fetch(`http://127.0.0.1:8080/mlfeats?session_id=${session_id}`)
    .then((res) => {
        return res.json()
    })
    .then((obj) => {
        return obj
    })
}


async function get_mlcluster(mlfs) {
    return await fetch(`http://127.0.0.1:8080/mlcluster`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify({
            mlfs: mlfs
        })
    })
    .then((res) => {
        return res.json()
    })
}

async function get_users(session_id) {
    return await fetch(`http://127.0.0.1:8080/users?session_id=${session_id}`)
    .then((res) => {
        return res.json()
    })
    .then((obj) => {
        return obj
    })
}


async function get_summary(messages, users) {
    return await fetch(`http://127.0.0.1:8080/summary`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify({
            messages: messages,
            users: users
        })
    })
    .then((res) => {
        return res.json()
    })
    .then((obj) => {
        return obj.choices[0].text
    }).catch(e => {
        console.log(e)
        return "ChatGPT not available at the moment."
    })
}



