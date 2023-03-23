'use strict';


window.addEventListener('load', async function () {
    const session_id = prompt("Please input session id: ")
    const chat = await get_chat(session_id)
    const users = await get_users(session_id)
    const messages = chat.messages
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
        c4.textContent = t
        c2.appendChild(c3)
        c1.appendChild(c2)
        c1.appendChild(c4)
        c0.appendChild(c1)
        node.appendChild(c0)
    }

    const node2 = document.getElementById("people");

    for (let i = 0; i < users.length; i++) {
        const c0 = document.createElement("li")
        const c1 = document.createElement("div")
        c1.className = "player-container"
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
        const c42 = this.document.createElement("option")
        c42.value = "permanent-ban"
        c42.textContent = "Permanent ban"
        const c43 = this.document.createElement("option")
        c43.value = "temporary-ban"
        c43.textContent = "Temporary ban"
        const c44 = this.document.createElement("option")
        c44.value = "ignore"
        c44.textContent = "Ignore"
        c3.appendChild(c41)
        c3.appendChild(c42)
        c3.appendChild(c43)
        c3.appendChild(c44)
        c1.appendChild(c2)
        c1.appendChild(c3)
        c0.appendChild(c1)
        node2.appendChild(c0)
    }



});

async function get_chat(session_id) {
    return await fetch(`http://127.0.0.1:8080/chat?session_id=${session_id}`)
    .then((res) => {
        return res.json()
    })
    .then((obj) => {
        // const messages_e = document.getElementById("messages");
        // const node = document.createElement("li");
        
        // obj.forEach(e => {
        //     const textnode = document.createTextNode(e);
        //     node.appendChild(textnode);
        //     const lb = document.createElement("br")
        //     node.appendChild(lb);
        // });

        // messages_e.appendChild(node)
        return obj
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
        
        console.log(obj)
        console.log(obj.choices[0].text)
        return obj.choices[0].text
    }).catch(e => {
        console.log(e)
        return "ChatGPT not available at the moment."
    })
}



