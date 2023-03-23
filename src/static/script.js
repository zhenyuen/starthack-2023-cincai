'use strict';


window.addEventListener('load', async function () {
    const session_id = prompt("Please input session id: ")
    const chat = await get_chat(session_id)
    const users = await get_users(session_id)
    const messages = chat.messages
    const timestamp = chat.timestamp
    const formatted = messages.map(function(e) { 
        return `${e.username}: ${e.message}`;
    });

    console.log(formatted)
    console.log(users)

    const summary = await get_summary(formatted, users)
    console.log(summary)
  
  
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
        const summary_e = document.getElementById("summary");
        console.log(obj)
        console.log(obj.choices[0].text)
        summary_e.textContent = obj.choices[0].text
        return obj.choices[0].text
    })
}



