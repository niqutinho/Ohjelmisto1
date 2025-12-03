let candidateCount = Number(prompt("Enter the number of candidates:"));

let candidates = [];
for (let i = 0; i < candidateCount; i++) {
    let name = prompt(`Name for candidate ${i + 1}`);
    candidates.push({ name: name, votes: 0 });
}

let voterCount = Number(prompt("Enter the number of voters:"));

for (let i = 0; i < voterCount; i++) {
    let vote = prompt(`Voter ${i + 1}, who do you vote for? (leave empty for blank vote)`);

    if (vote === "") {
        continue;
    }

    let found = false;
    for (let cand of candidates) {
        if (cand.name.toLowerCase() === vote.toLowerCase()) {  // case-insensitive
            cand.votes++;
            found = true;
            break;
        }
    }
    if (!found) {
        alert("Invalid candidate name – vote ignored!");
    }
}

let maxVotes = 0;
let winner = null;

for (let cand of candidates) {
    if (cand.votes > maxVotes) {
        maxVotes = cand.votes;
        winner = cand;
    }
}

candidates.sort((a, b) => b.votes - a.votes);

console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
console.log("results:");
for (let cand of candidates) {
    console.log(`${cand.name}: ${cand.votes} votes`);
}