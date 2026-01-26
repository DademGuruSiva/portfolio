function showOverlay(overlayId, pageUrl) {
    var overlay = document.getElementById(overlayId);
    var iframe = overlay.querySelector('#invisibleFrame');
    iframe.src = pageUrl;
    overlay.style.display = 'block';
}

function hideOverlay(overlayId) {
    var overlay = document.getElementById(overlayId);
    overlay.style.display = 'none';
}
