function buttonClick() {
    var x = document.getElementById("topdown");

    if (x.style.display !== "none") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

function ball() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "block";
    yn.style.display = "none";
    ym.style.display = "none";
    yt.style.display = "none";
    m.style.display = "none";
    t.style.display = "none";
    n.style.display = "none";

}
function byn() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "block";
    ym.style.display = "none";
    yt.style.display = "none";
    m.style.display = "none";
    t.style.display = "none";
    n.style.display = "none";

}
function bym() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "none";
    ym.style.display = "block";
    yt.style.display = "none";
    m.style.display = "none";
    t.style.display = "none";
    n.style.display = "none";

}
function byt() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "none";
    ym.style.display = "none";
    yt.style.display = "block";
    m.style.display = "none";
    t.style.display = "none";
    n.style.display = "none";

}
function bm() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "none";
    ym.style.display = "none";
    yt.style.display = "none";
    m.style.display = "block";
    t.style.display = "none";
    n.style.display = "none";

}
function bt() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "none";
    ym.style.display = "none";
    yt.style.display = "none";
    m.style.display = "none";
    t.style.display = "block";
    n.style.display = "none";

}
function bn() {
    var all = document.getElementById("all");
    var yn = document.getElementById("yn");
    var ym = document.getElementById("ym");
    var yt = document.getElementById("yt");
    var m = document.getElementById("m");
    var t = document.getElementById("t");
    var n = document.getElementById("n");

    all.style.display = "none";
    yn.style.display = "none";
    ym.style.display = "none";
    yt.style.display = "none";
    m.style.display = "none";
    t.style.display = "none";
    n.style.display = "block";

}

function startLoading() {
    const loadingContainer = document.getElementById('loading-container');
    loadingContainer.style.display = 'block';

    const loadingBar = document.getElementById('loading-bar');
    const loadingText = document.getElementById('loading-text');

    let progress = 0;
    const interval = 1000; // 1 second interval
    const totalTime = 10000; // 17 seconds

    function updateLoadingBar() {
        progress += (interval / totalTime) * 100;
        loadingBar.style.width = `${progress}%`;
        loadingText.innerText = `Loading... ${Math.round(progress)}%`;

        if (progress >= 100) {
            clearInterval(loadingInterval);
            loadingText.innerText = 'Loading completing... hang on a second!';
        }
    }

    const loadingInterval = setInterval(updateLoadingBar, interval);
}


