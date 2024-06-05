function myfunction() {
  var x = document.getElementById("speechtotext");
  var y = document.getElementById("btncon");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
    y.style.display = "flex";
  }
}

function myfunction2() {
  var x = document.getElementById("speechtotext");
  var y = document.getElementById("btncon");
  if (y.style.display === "none") {
    y.style.display = "flex";
    x.style.display = "none";
  } else {
    y.style.display = "none";
    x.style.display = "block";
  }
  document.getElementById("text").textContent = "";
}

function myfunction3() {
  var x = document.getElementById("texttospeech");
  var y = document.getElementById("btncon");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
    y.style.display = "flex";
  }
}

function myfunction4() {
  var x = document.getElementById("texttospeech");
  var y = document.getElementById("btncon");
  if (y.style.display === "none") {
    y.style.display = "flex";
    x.style.display = "none";
  } else {
    y.style.display = "none";
    x.style.display = "block";
  }
  document.getElementById("area").value = "";
  document.getElementById("text1").textContent = "";
}

function myfunction5() {
  var x = document.getElementById("opentask");
  var y = document.getElementById("btncon");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
    y.style.display = "flex";
  }
}

function myfunction6() {
  var x = document.getElementById("opentask");
  var y = document.getElementById("btncon");
  if (y.style.display === "none") {
    y.style.display = "flex";
    x.style.display = "none";
  } else {
    y.style.display = "none";
    x.style.display = "block";
  }
  document.getElementById("text2").textContent = "";
  document.getElementById("url").value = "";
  document.getElementById("command").value = "";
}

function func() {
  var x = document.getElementById("speechtotext");
  var z = document.getElementById("texttospeech");
  var a = document.getElementById("opentask");
  var y = document.getElementById("btncon");
  if (y.style.display === "none") {
    y.style.display = "flex";
    x.style.display = "none";
    z.style.display = "none";
    a.style.display = "none";
  }
  document.getElementById("text").textContent = "";
  document.getElementById("area").value = "";
  document.getElementById("text1").textContent = "";
  document.getElementById("text2").textContent = "";
  document.getElementById("url").value = "";
  document.getElementById("command").value = "";
}