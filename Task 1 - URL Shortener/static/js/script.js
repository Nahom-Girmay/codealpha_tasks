function copyLink() {

  const link = document.getElementById("short-link");

  navigator.clipboard.writeText(link.innerText);

  const button = document.getElementById("copy-button");

  button.innerText = "Copied! ✓";

  setTimeout(function(){

    button.innerText = "Copy Link";

  },2000);

}