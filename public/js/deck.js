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
var gid = 0;

async function fetchDB(file) {
	let response = await fetch(file);
	let data = await response.json();
	console.log(data)
	return data;
}
function randId(db) {
	let target = db[Math.floor(Math.random() * db.length)];
	return target.goldenId || target.id;
}
async function initBoard() {
	window.database = await fetchDB("/data.json");
	window.battle = await fetchDB("/battle.json");
	function addMinion(position, index) {
		battle[0][0][position].forEach(minion => {
			let prop = {
				attack: minion.atk,
				health: minion.health,
				belongsTo: index,
				id: "TB_BaconUps_038",//randId(database),//"TB_BaconUps_080",
				gid: minion.id,
				poisonous: minion.poison,
				shield: minion.shield,
				taunt: minion.taunt,
				golden: minion.golden
			};
			minions[minion.id] = new Minion(prop);
		});
	}
	addMinion("up", 0);
	addMinion("down", 1);
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

function Minion(prop) {
	this.prop = prop;
	this.ele = document.createElement("div");
	this.ele.setAttribute("gid", this.prop.gid);
	this.dbIndex = database.findIndex(item => [item.id, item.goldenId].includes(this.prop.id));
	this.data = database[this.dbIndex];
	this.dead = false;
	this.ele.insertAdjacentHTML("afterbegin", `
			<div class="image art"></div>
			<div class="image border"></div>
			<div class="image taunt"></div>
			<div class="image legendary"></div>
			<div class="image deathrattle"></div>
			<div class="image trigger"></div>
			<div class="image poison"></div>
			<div class="image atk-health"></div>
			<div class="text attack">${this.prop.attack}</div>
			<div class="text health">${this.prop.health}</div>
			<div class="image shield"></div>
			<div class="image shield"></div>`);
	this.ele.querySelector(".art").style.backgroundImage = `url(https://art.hearthstonejson.com/v1/256x/${this.prop.id}.jpg)`;
	document.querySelectorAll(`.minions`)[this.prop.belongsTo].appendChild(this.ele);
	this.initClassName = function() {
		this.ele.classList.add("minion");
		//if (this.data.goldenId === this.prop.id) this.ele.classList.add("golden");
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
			this.ele.classList.add("lose-shield");
			setTimeout(() => {
				this.ele.classList.remove("shield", "lose-shield");
			}, 2000);
			return this.splat("-0");
		}
	}
	this.setHealth = function(health) {
		let deltaHealth = health - this.prop.health;
		this.prop.health = health;
		this.ele.querySelector(".text.health").innerText = this.prop.health;
		if (deltaHealth < 0) {
			this.ele.querySelector(".health").classList.add("text-splat");
			setTimeout(() => {
				this.ele.querySelector(".health").classList.remove("text-splat");
			}, 1000)
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
			setTimeout(resolve, 1500);
		});
	}
	this.setAttack = function(attack) {
		this.prop.attack = attack;
		this.ele.querySelector(".text.attack").innerText = this.prop.attack;
	}
	this.doAttack = function(target) {
		if (this.dead) return;
		let targetEle = minions[target].ele;
		let deltaX = targetEle.getBoundingClientRect().x - this.ele.getBoundingClientRect().x;
		let deltaY = targetEle.getBoundingClientRect().y - this.ele.getBoundingClientRect().y;
		//deltaX > 0 ? deltaX -= this.ele.offsetWidth / 3 : deltaX += this.ele.offsetWidth / 3;
		//deltaY > 0 ? deltaY -= this.ele.offsetHeight / 3 : deltaY += this.ele.offsetHeight / 3;
		document.querySelectorAll(".minions")[this.prop.belongsTo].style.cssText = "z-index: 100;";
		document.querySelectorAll(".minions")[1 - this.prop.belongsTo].style.cssText = "z-index: 0;";
		console.log("STYLE", new Date().getSeconds(), new Date().getMilliseconds())
		let rid = makeid(8);
		document.getElementById("attack-style").innerHTML += `@keyframes attacking-${rid} {
				0% {
					transform: translate3d(0, 0, 0);
				}
				40% {
					transform: translate3d(0, 0, 2vw);
				}
				60% {
					transform: translate3d(${deltaX}px, ${deltaY}px, 0);
				}
				61% {
					transform: translate3d(${deltaX}px, ${deltaY}px, 0) rotateX(-30deg);
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
		this.ele.classList.add(`attacking-${rid}`);
		console.log("ATK", new Date().getSeconds(), new Date().getMilliseconds())
		return new Promise(resolve => {
			setTimeout(() => {
				document.querySelector(".section-decklist").classList.add(this.prop.belongsTo === 0 ? "shake-down" : "shake-up");
				resolve();
				console.log("RESOLVE", new Date().getSeconds(), new Date().getMilliseconds())
				setTimeout(() => {
					document.querySelector(".section-decklist").classList.remove(this.prop.belongsTo === 0 ? "shake-down" : "shake-up");
					this.ele.classList.remove(`attacking-${rid}`);
					console.log("STOP", new Date().getSeconds(), new Date().getMilliseconds())
				}, 500);
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
		}
		this.ele.classList.add("dying");
		setTimeout(() => {
			if (animEle) {
				document.body.appendChild(animEle);
				setTimeout(() => {
					document.body.removeChild(animEle);
				}, 4000);
			}
			this.ele.parentNode.removeChild(this.ele);
		}, 1500);
		return new Promise(resolve => {
			setTimeout(resolve, 500);
		});
	}
}

(async () => {
	await initBoard();
	//var queue = [];
	document.getElementById("console").innerText = battle[2];
	for (let i in battle[1]) {
		i = Number(i);
		let attacking = battle[1][i];
		let result = battle[0][i + 1];
		let queue = {
			health: [],
			die: []
		};
		for (let i in minions) {
			let minion = minions[i];
			if (minion.dead) continue;
			let downIndex = result.down.findIndex(ele => {
				return ele.id === minion.prop.gid;
			});
			let upIndex = result.up.findIndex(ele => ele.id === minion.prop.gid);
			//console.log(downIndex, upIndex);
			if (downIndex === -1 && upIndex === -1) queue.die.push(() => minion.die());//可以移除
			else {
				let target;
				if (downIndex !== -1) {
					target = result.down[downIndex];
					queue.health.push(() => minion.setHealth(target.health));
					queue.health.push(() => minion.setAttack(target.atk));
					queue.health.push(() => minion.setShield(target.shield));
					if (target.death) queue.die.push(() => minion.die());
				} else {
					target = result.up[upIndex];
					queue.health.push(() => minion.setHealth(target.health));
					queue.health.push(() => minion.setAttack(target.atk));
					queue.health.push(() => minion.setShield(target.shield));
					if (target.death) queue.die.push(() => minion.die());
				}
			}
		}
		if (attacking.length === 2) await minions[attacking[0]].doAttack(attacking[1]);
		if (typeof battle[3] === "number") {
			await new Promise(resolve => {
				setTimeout(resolve, battle[3]);
			});
		}
		await Promise.all(queue.health.map(ele => ele()));
		await Promise.all(queue.die.map(ele => ele()));
	}
})();
/*

document.querySelectorAll(".minion").forEach(ele => {
	//ele,
});
	for (let i = 0; i < 7; i++) {
		let prop = {
			attack: 7,
			health: 10,
			belongsTo: 0,
			id: "TB_BaconUps_093",//randId(database),//"TB_BaconUps_080",
			gid
		}
		let minion = new Minion(prop);
		minions[gid++] = minion;
	}
	for (let i = 0; i < 7; i++) {
		let prop = {
			attack: 7,
			health: 10,
			belongsTo: 1,
			id: "TB_BaconUps_093",//randId(database),//"TB_BaconUps_099",
			gid
		}
		let minion = new Minion(prop);
		minions[gid++] = minion;
	}
var queue = [
	() => minions[0].doAttack(8),
	[() => minions[8].setHealth(3), () => minions[0].setHealth(3)],
	() => minions[0].doAttack(8),
	[() => minions[8].setHealth(-4), () => minions[0].setHealth(-4)],
	[() => minions[8].die(), () => minions[0].die()]
];
async function animation(queue) {
	for (let anim of queue) {
		if (typeof anim === "function") {
			await anim();
		} else {
			await Promise.all(anim.map(ele => ele()));
		}
	}
}

animation(queue);
*/
