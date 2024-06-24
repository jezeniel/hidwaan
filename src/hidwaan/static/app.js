window.hidwaan = (function () {
  var app = {};

  app.servers = function () {
    return {
      showCreateModal: false,
      servers: [],
      serversLoaded: false,
      serverForm: {
        name: "",
        description: "",
      },
      submitForm: async function () {
        const response = await fetch("/servers", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.serverForm),
        });

        const data = await response.json();
        this.servers.push(data);
        this.showCreateModal = false;
      },
      getServers: async function () {
        const response = await fetch("/servers", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        this.servers = await response.json();
        this.serversLoaded = true;
      },
      toggleCreateModal: function () {
        var modal = document.getElementById("create_server_dialog");
        this.showCreateModal = !this.showCreateModal;
        if (this.showCreateModal) {
          modal.showModal();
        } else {
          modal.close();
        }
      },
    };
  };

  app.chat = function () {
    return {
      messages: [],
      inputMessage: "",
      username: "",
      socket: null,
      connected: false,
      connectws: function () {
        this.socket = new WebSocket("ws://localhost:8000/ws");
        this.socket.onopen = function (event) {
          this.connected = true;
          this.socket.send(JSON.stringify({ type: "JOIN" }));
          this.username = prompt("Enter nickname", "");
        }.bind(this);

        this.socket.onmessage = function (event) {
          var data = JSON.parse(event.data);
          if (data.type == "MSG") {
            this.messages.push({ username: data.username, text: data.text });
          }
        }.bind(this);
      },
      sendMessage: function () {
        var message = {
          username: this.username,
          text: this.inputMessage,
          type: "MSG",
        };
        this.socket.send(JSON.stringify(message));
        this.inputMessage = "";
      },
    };
  };

  return app;
})();
