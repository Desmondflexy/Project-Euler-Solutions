// Problem 54: Poker hands
const card_suits = ['C', 'S', 'D', 'H'];  // -> club[C], spade[S], diamond[D], heart[H]
const card_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'];

//SAMPLE INPUT
player_1 = ['JD', 'TD', 'AD', 'KD', 'QD'];

/**Returns the rank of a hand in the card game of poker.*/
function rank(hand) {
    // Royal flush -- 10
    const hand_values = hand.map(i => i[0]);
    const big_card_values = card_values.slice(8);
    if (big_card_values.every(i => hand_values.includes(i)) && is_same_suit()) return 10;

    // Straight flush -- 9
    if (isconsecutive() && is_same_suit()) return 9;
    // Four of a kind -- 8
    if (n_of_a_kind(4) > 0) return 8;
    // Full house -- 7
    if (n_of_a_kind(3) > 0 && n_of_a_kind(2)) return 7;
    // Flush -- 6
    if (is_same_suit()) return 6;
    // Straight -- 5
    if (isconsecutive()) return 5;
    // Three of a kind -- 4
    if (n_of_a_kind(3) > 0) return 4;
    // Two pair
    if (n_of_a_kind(2) > 1) return 3;
    // One pair -- 2 otherwise High card -- 1
    return n_of_a_kind(2) > 0 ? 2 : 1;


    /**Checks if card values are consecutive */
    function isconsecutive() {
        const d = hand.map(i => card_values.indexOf(i[0]));
        d.sort((a, b) => a - b);
        const a = d.map(i => card_values[i]).join('');
        const b = card_values.join('');
        for (let i = 0; i < b.length - 5; i++) {
            if (a === b.slice(i, i + 5)) return true;
        }
        return false;
    }

    /**Returns number of occurrence of n of a kind. */
    function n_of_a_kind(n) {
        const kind = {};
        for (let i = 0; i < hand.length; i++) {
            val = hand[i][0];
            if (!Object.keys(kind).includes(val)) {
                kind[val] = 1;
            } else {
                kind[val]++;
            }
        }
        return count(Object.values(kind), n);
    }

    /**Checks if cards are same suit. */
    function is_same_suit() {
        const hand_suits = hand.map(i => i[1]);
        const unique_hand_suits = new Set(hand_suits);
        return Array.from(unique_hand_suits).length === 1;
    }
}


/**Converts cards in hand to values in descending order. */
function handvalue(hand) {
    const val = hand.map(card => card[0]);
    const lst = val.map(v => card_values.indexOf(v) + 2);
    return lst.map(i => i).sort((x, y) => y - x);
}

fetch('./p054_poker.json')
    .then(response => response.json())
    .then(obj => {
        const book = Object.values(obj);
        let player1_wins = 0;
        let results = 0;
        for (let i = 0; i < book.length; i++) {
            const hand = book[i].split(' ');
            const player1 = hand.slice(0, 5);
            const player2 = hand.slice(5,);
            const r1 = rank(player1);
            const r2 = rank(player2);

            let winner;
            if (r1 > r2) {
                player1_wins++;
                winner = 'player1 wins (rank)';
            } else if (r1 < r2) {
                winner = 'player2 wins (rank)';
            } else {
                const p1 = handvalue(player1);
                const p2 = handvalue(player2);
                const a = p1.map(i => count(p1, i));
                const n1 = p1[a.indexOf(2)];
                const b = p2.map(i => count(p2, i));
                const n2 = p2[b.indexOf(2)];

                if (n1 > n2) {
                    player1_wins++;
                    winner = 'player1 wins (one pair)';
                } else if (n1 < n2) {
                    winner = 'player2 wins (one pair)';
                } else {
                    for (let i = 0; i < 2; i++) {
                        p1.splice(p1.indexOf(n1), 1);
                        p2.splice(p2.indexOf(n2), 1);
                    }
                    if (arrayCompare(p1, p2) > 0) {
                        player1_wins++;
                        winner = 'player1 wins (one pair, highest cards)';
                    } else if (arrayCompare(p1, p2) < 0) {
                        winner = 'player2 wins (one pair, highest cards)';
                    } else {
                        winner = 'draw';
                    }
                }
            }
            const x = 1;
            if ((r1 >= x || r2 >= x) && winner.includes('player1')) {
                results++;
                console.log(`[${player1}] ${r1} -- ${r2} [${player2}] -- ${winner}`);
            }
        }
        console.log(results);
        document.body.innerHTML = `Euler Problem 54<br>Poker hands`;

    })


/**Returns the number of occurence of an element in an array */
function count(arr, elem) {
    return arr.filter(i => i === elem).length;
}

/**Compare two arrays -- arr1 > arr2*/
function arrayCompare(arr1, arr2) {
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] > arr2[i]) return 1;
        if (arr1[i] < arr2[i]) return -1;
        if (arr1[i] === arr2[i]) continue;
    }
    return 0;
}