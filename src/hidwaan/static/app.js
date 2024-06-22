window.hidwaan = (function () {
  var app = {};

  app.servers = function () {
    return {
      showCreateModal: false,
      servers: [],
      serversLoaded: false,
      getServers: async function () {
        console.log("get servers!");
        var response = await fetch("/servers", {
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
      },
    };
  };

  return app;
})();
