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

  return app;
})();
