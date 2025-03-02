
//# Author: Shivani Jariwala and Aishwarya Indi
//# Team Puma
function showMessage(message, isError = false) {
    const messageBox = document.getElementById("messageBox");
    messageBox.innerHTML = message;
    messageBox.style.color = isError ? "red" : "green";
}

async function createPost() {
    const content = document.getElementById("postContent").value;
    const response = await fetch("/post", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
    });

    const data = await response.json();
    if (response.ok) {
        showMessage("Post Created! ID: " + data.id);
    } else {
        showMessage("Error: " + data.error, true);
    }
}

async function getPost() {
    const postId = document.getElementById("postId").value;
    const response = await fetch(`/get/${postId}`);

    const data = await response.json();
    if (response.ok) {
        showMessage("Post: " + data.content + " (Created At: " + data.created_at + ")");
    } else {
        showMessage("Error: " + data.error, true);
    }
}

async function deletePost() {
    const postId = document.getElementById("postId").value;
    const response = await fetch(`/delete/${postId}`, { method: "DELETE" });

    const data = await response.json();
    if (response.ok) {
        showMessage("Post Deleted!");
    } else {
        showMessage("Error: " + data.error, true);
    }
}

async function getUserDetails() {
    const response = await fetch("/user");

    const data = await response.json();
    if (response.ok) {
        showMessage(`User: ${data.username}, Followers: ${data.followers}, Following: ${data.following}, Posts: ${data.statuses}`);
    } else {
        showMessage("Error: " + data.error, true);
    }
}