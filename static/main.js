window.scrollTo = function () {
};
document.getElementById("iframe").addEventListener("load", function () {
    document.body.focus()
})

window.HELP_IMPROVE_VIDEOJS = false
let liveui = !videojs.browser.IS_ANDROID
const vid = document.getElementById('vid1');
const player = videojs(vid, {
    liveui: liveui,
    liveTracker: {
        trackingThreshold: 0,
    },
    aspectRatio: '16:9'
});
player.play();
let qualityLevels = player.qualityLevels();
qualityLevels.on('addqualitylevel', function (event) {
    let qualityLevel = event.qualityLevel;
    console.info(qualityLevel)
});
player.hlsQualitySelector();
const displayModeNames = {"regular": "Regular", "side-by-side": "Side-by-side View", "no-chat": "Hidden Chat"}
const chatWrapper = document.getElementById("chat-wrapper")

function setDisplayMode() {
    document.body.className = displayMode
    localStorage.setItem("displayMode", displayMode)
    if (displayMode === "no-chat") {
        document.querySelector("iframe").remove()
    } else if (!document.querySelector("iframe")) {
        window.location.reload()
    }
    if (displayMode === "side-by-side") {
        chatWrapper.classList.remove("ratio")
    } else {
        chatWrapper.classList.add("ratio")

    }
    document.getElementById("side-by-side-button").innerText = displayModeNames[displayMode]
}


const stored = localStorage.getItem("displayMode")
let displayMode;
if (stored) {
    displayMode = stored
} else {
    displayMode = "regular"
}
setDisplayMode()
document.getElementById("side-by-side-button").addEventListener("click", function () {
    switch (displayMode) {
        case "regular":
            displayMode = "side-by-side"
            break
        case "side-by-side":
            displayMode = "no-chat"
            break
        case "no-chat":
            displayMode = "regular"
            break
    }
    setDisplayMode()
})
