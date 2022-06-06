htmx.defineExtension("pico-busy", {
  onEvent: function (name, evt) {
    var elt = evt.detail.elt;
    var submitBtn = elt.querySelector('button[type="submit"]')
    if (name === "htmx:beforeRequest") {
      submitBtn.setAttribute("aria-busy", "true");
    } else if (name === "htmx:afterRequest") {
      submitBtn.setAttribute("aria-busy", "false");
    }
  },
});
