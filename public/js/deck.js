function setSize() {
	let height = Math.min(window.innerWidth * 10 / 12, window.innerHeight);
	let width = Math.min(window.innerWidth, window.innerHeight * 12 / 10);
	document.querySelector(".section-decklist").style.width = width + "px";
	document.querySelector(".section-decklist").style.height = height + "px";
	document.querySelector(".section-decklist").style.marginTop = (window.innerHeight - height) / 2 + "px";
}
setSize();
window.addEventListener("resize", setSize);
var minions = [];

function toggleMenu() {
	let target = document.getElementById("menu");
	target.style.display = (target.style.display === "block") ? "none" : "block";
}
function toggleConsole() {
	let target = document.getElementById("console");
	target.style.display = (target.style.display === "block") ? "none" : "block";
}

async function fetchDB(file) {
	let response = await fetch(file);
	let data = await response.json();
	console.log(data);
	return data;
}
async function initBoard() {
	window.database = await fetchDB("/data.json");
	window.battle = await fetchDB("/battle.json");
	["up", "down"].forEach(board => battle[0][0][board].forEach(prop => minions[prop.id] = new Minion(prop, board)));
}

function makeid(length) {
	var result = '';
	var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	var charactersLength = characters.length;
	for (var i = 0; i < length; i++) {
		result += characters.charAt(Math.floor(Math.random() * charactersLength));
	}
	return result;
}

function Minion(prop, board, position) {
	let index = database.findIndex(item => prop.name.toLowerCase() === item.name.toLowerCase());
	//this.dbIndex = database.findIndex(item => [item.id, item.goldenId].includes(this.id));
	this.data = database[index];
	this.id = (index !== -1) ? ((prop.golden && database[index].goldenId) ? database[index].goldenId : database[index].id) : "TB_BaconUps_038";
	this.gid = prop.id;
	this.prop = prop;
	this.ele = document.createElement("div");
	this.ele.setAttribute("gid", this.gid);
	this.belongsTo = ["up", "down"].indexOf(board);
	this.parent = document.querySelectorAll(`.minions`)[this.belongsTo];
	this.dead = false;
	this.ele.insertAdjacentHTML("afterbegin", `
			<div class="image art"></div>
			<div class="image border"></div>
			<div class="image taunt"></div>
			<div class="image legendary"></div>
			<div class="image deathrattle"></div>
			<div class="image trigger"></div>
			<div class="image poisonous"></div>
			<div class="image atk-health"></div>
			<div class="text attack">${this.prop.attack}</div>
			<div class="text health">${this.prop.health}</div>
			<div class="image shield"></div>
			<div class="preview">
				<img loading="lazy" src="https://art.hearthstonejson.com/v1/render/latest/${"zhCN"}/256x/${this.id}.png">
			</div>`);
	this.ele.querySelector(".art").style.backgroundImage = `url(https://art.hearthstonejson.com/v1/256x/${this.id}.jpg)`;
	if ((typeof position === "number") && (position < this.parent.querySelectorAll(".minion:not(.dying)").length)) {
		this.parent.querySelectorAll(".minion:not(.dying)")[position].insertAdjacentElement("beforebegin", this.ele);
	}
	else this.parent.appendChild(this.ele);
	this.animationTimer = function(target, className) {
		return new Promise(resolve => {
			target.classList.add(className);
			let listener = target.addEventListener("animationend", () => {
				target.classList.remove(className);
				target.removeEventListener("animationend", listener);
				resolve();
			});
		});
	}
	this.summon = function() {
		this.ele.classList.remove("before-summon");
		return this.animationTimer(this.ele, "summon");
	}
	this.initClassName = function() {
		this.ele.classList.add("minion");
		if (this.prop.source !== "origin") this.ele.classList.add("before-summon");
		//if (this.data.goldenId === this.id) this.ele.classList.add("golden");
		if (this.prop.golden) this.ele.classList.add("golden");
		if (this.data.divineShield) this.ele.classList.add("shield");
		if (this.data.cleave) this.ele.classList.add("trigger");
		["legendary", "taunt", "poisonous", "windfury", "deathrattle", "shield"].forEach(item => {
			if (this.data[item] || this.prop[item]) this.ele.classList.add(item);
		});
	}
	this.initClassName();
	this.setShield = function(state) {
		if (this.prop.shield === state) return;
		this.prop.shield = state;
		if (state) this.ele.classList.add("shield");
		else {
			this.ele.classList.remove("shield");
			this.animationTimer(this.ele, "lose-shield");
			return this.splat("-0");
		}
	}
	this.setHealth = function(health) {
		let deltaHealth = health - this.prop.health;
		this.prop.health = health;
		this.ele.querySelector(".text.health").innerText = this.prop.health;
		if (deltaHealth < 0) {
			this.animationTimer(this.ele.querySelector(".health"), "text-splat");
			return this.splat(deltaHealth);
		}
	}
	this.splat = function(value) {
		var animEle = document.createElement("div");
		animEle.classList.add("image", "blood-splat");
		animEle.innerHTML = `<div class="text blood-splat">${value}</div>`;
		this.ele.appendChild(animEle);
		setTimeout(() => {
			this.ele.removeChild(animEle);
		}, 2900);
		return new Promise(resolve => {
			setTimeout(resolve, 1000);
		});
	}
	this.getPosition = function() {
		let allMinions = this.parent.querySelectorAll(".minion:not(.before-summon)");
		return [...allMinions].indexOf(this.ele) - allMinions.length / 2;
	}
	this.setAttack = function(attack) {
		let deltaAttack = attack - this.prop.attack;
		this.prop.attack = attack;
		this.ele.querySelector(".text.attack").innerText = this.prop.attack;
		if (deltaAttack !== 0) {
			this.animationTimer(this.ele.querySelector(".attack"), "text-splat");
		}
	}
	this.doAttack = function(targetId) {
		if (this.dead) return;
		let target = minions[targetId];
		let deltaX = (target.getPosition() - this.getPosition()) * 100;
		let deltaY = this.belongsTo === 0 ? 100 : -100;
		this.parent.style.cssText = "z-index: 100;";
		document.querySelectorAll(".minions")[1 - this.belongsTo].style.cssText = "z-index: 0;";
		let rid = makeid(8);
		document.getElementById("attack-style").innerHTML += `@keyframes attacking-${rid} {
				0% {
					transform: translate3d(0, 0, 0);
				}
				40% {
					transform: translate3d(0, 0, 2vw);
				}
				60% {
					transform: translate3d(${deltaX}%, ${deltaY}%, 0);
				}
				61% {
					transform: translate3d(${deltaX}%, ${deltaY}%, 0) rotateX(-30deg);
				}
				80% {
					transform: translate3d(0, 0, 0) rotateX(-30deg);
				}
				100% {
					transform: translate3d(0, 0, 0);
				}
			}
			.attacking-${rid} {
				animation: attacking-${rid} 1s;
				z-index: 100;
			}
			`;
		this.animationTimer(this.ele, `attacking-${rid}`);
		return new Promise(resolve => {
			setTimeout(() => {
				this.animationTimer(document.querySelector(".section-decklist"), this.belongsTo === 0 ? "shake-down" : "shake-up");
				resolve();
			}, 500);
		});
	}
	this.createOverlayAnim = function(className) {
		var animEle = document.createElement("div");
		animEle.classList.add("overlay", className);
		animEle.style.left = this.ele.getBoundingClientRect().left + this.ele.offsetWidth / 2 + "px";
		animEle.style.bottom = window.innerHeight - this.ele.getBoundingClientRect().bottom + "px";
		animEle.style.width = this.ele.offsetWidth + "px";
		animEle.style.height = this.ele.offsetHeight + "px";
		return animEle;
	}
	this.die = function() {
		if (this.dead) return;
		this.dead = true;
		if (this.data.deathrattle) {
			var animEle = this.createOverlayAnim("deathrattle-die");
			document.body.appendChild(animEle);
			setTimeout(() => {
				document.body.removeChild(animEle);
			}, 4000);
		}
		this.ele.classList.add("dying");
		setTimeout(() => {
			this.ele.parentNode.removeChild(this.ele);
		}, 1500);
		return new Promise(resolve => {
			setTimeout(resolve, 500);
		});
	}
}

(async () => {
	await initBoard();
	document.getElementById("console").innerText = battle[2];
	for (let i in battle[1]) {
		i = Number(i);
		let attacking = battle[1][i];
		let result = battle[0][i + 1];
		let queue = {
			health: [],
			die: [],
			summon: {
				before: [],
				after: []
			}
		};
		["up", "down"].forEach(board => {
			result[board].forEach((target, position) => {
				let minion = minions[target.id];
				if (!minion) {
					minion = minions[target.id] = new Minion(target, board, position);
					if (["damage", "overkill"].includes(minion.prop.source)) queue.summon.before.push(() => minion.summon());
					else queue.summon.after.push(() => minion.summon());
					return;
				}
				queue.health.push(() => minion.setShield(target.shield));
				queue.health.push(() => minion.setAttack(target.attack));
				queue.health.push(() => minion.setHealth(target.health));
				if (target.death) queue.die.push(() => minion.die());
			});
		});
		if (attacking.length === 2) await minions[attacking[0]].doAttack(attacking[1]);
		await Promise.all(queue.die.map(ele => ele()));
		await Promise.all(queue.health.map(ele => ele()));
		await Promise.all(queue.summon.before.map(ele => ele()));
		await Promise.all(queue.summon.after.map(ele => ele()));
		if (typeof battle[3] === "number") {
			await new Promise(resolve => {
				setTimeout(resolve, battle[3]);
			});
		}
	}
})();
