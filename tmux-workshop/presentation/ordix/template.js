function initialize() {
	changeCSS();
	changeSlideTitle();
}

function changeCSS() {
	let slideNumber = document.getElementsByClassName("slide-number")[0];
	slideNumber.style.backgroundColor = "rgba(0, 0, 0, 0)";
	slideNumber.style.color = "#111111";
	slideNumber.style.fontSize = "16px";

	document.getElementsByClassName("progress")[0].style.height = "6px";

	document.getElementsByClassName("navigate-left")[0].style.right = "10em";
	document.getElementsByClassName("navigate-right")[0].style.right = "4em";
}

function showHeaderFooter() {
	const templateHeader = document.getElementById("header");
	templateHeader.style.display = "block";

	const templateFooter = document.getElementById("footer");
	templateFooter.style.display = "block";
}

function hideHeaderFooter() {
	const templateHeader = document.getElementById("header");
	templateHeader.style.display = "none";

	const templateFooter = document.getElementById("footer");
	templateFooter.style.display = "none";
}

function showStartPage(progress) {
	let startpage = document.getElementById("startpage");
	let newStartpage = document.getElementById("newStartpage");

	// initial
	if (progress === 0) {
		startpage.style.display = "none";
		newStartpage.style.display = "block";
	} else {
		startpage.style.display = "block";
		newStartpage.style.display = "none";
	}
}

function showEndPage(progress) {
	let endpage = document.getElementById("endpage");
	let newEndpage = document.getElementById("newEndpage");

	// initial
	if (progress === 1) {
		endpage.style.display = "none";
		newEndpage.style.display = "block";
	} else {
		endpage.style.display = "block";
		newEndpage.style.display = "none";
	}
}

function changeSlideTitle() {
	if (Reveal.getProgress() == 0 || Reveal.getProgress() == 1) {
		hideHeaderFooter();
	} else {
		showHeaderFooter();
	}
	showStartPage(Reveal.getProgress());
	showEndPage(Reveal.getProgress());

	let titleElement = document.getElementById("masterTitle");
	try {
		titleElement.textContent = Reveal.getCurrentSlide().title;
	} catch {
		titleElement.textContent = "";
	}
}

window.onload = function () {
	initialize();
};

document.getElementsByClassName("navigate-right")[0].onclick = function () {
	changeSlideTitle();
};

document.getElementsByClassName("navigate-up")[0].onclick = function () {
	changeSlideTitle();
};

document.getElementsByClassName("navigate-down")[0].onclick = function () {
	changeSlideTitle();
};

document.getElementsByClassName("navigate-left")[0].onclick = function () {
	changeSlideTitle();
};

document.addEventListener("keydown", function (event) {
	changeSlideTitle();
});

document.addEventListener("keyright", function (event) {
	changeSlideTitle();
});

document.addEventListener("keyup", function (event) {
	changeSlideTitle();
});

document.addEventListener("keyleft", function (event) {
	changeSlideTitle();
});
