const TITLE = "Blackscreen Simulator - Tmux";
const SPEAKER = "lck";
const PLACE = "Wiesbaden";

Date.prototype.today = function () {
	return (
		(this.getDate() < 10 ? "0" : "") +
		this.getDate() +
		"." +
		(this.getMonth() + 1 < 10 ? "0" : "") +
		(this.getMonth() + 1) +
		"." +
		this.getFullYear()
	);
};

let test = new Date().today();

let titleContainer = document.getElementsByClassName("title");
let placeContainer = document.getElementsByClassName("place");
let dateContainer = document.getElementsByClassName("date");
let speakerContainer = document.getElementsByClassName("speaker");

for (i = 0; i < titleContainer.length; i++) {
	titleContainer[i].textContent = TITLE;
}

for (i = 0; i < placeContainer.length; i++) {
	placeContainer[i].textContent = PLACE;
}

for (i = 0; i < dateContainer.length; i++) {
	dateContainer[i].textContent = test;
}

for (i = 0; i < speakerContainer.length; i++) {
	speakerContainer[i].textContent = SPEAKER;
}
