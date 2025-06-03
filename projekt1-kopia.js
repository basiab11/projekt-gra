let flipped=[];
let moves=0;

function flipCard(card){
    if (card.classList.contains('flipped')||card.classList.contains('matched')||flipped.length>=2)return;

    card.classList.add("flipped");
    card.textContent=card.dataset.value;
    flipped.push(card);

    if (flipped.length===2){
        moves++;
        document.getElementById("moveCount").textContent=moves;
        
        if(flipped[0].dataset.pairId === flipped[1].dataset.pairId){
            flipped.forEach(c=>c.classList.add('matched'));
            flipped =[];
            checkWin();
        } else {
            setTimeout(()=> {
                flipped.forEach(c => {
                    c.classList.remove('flipped');
                    c.textContent="?"
                });
                flipped=[];
            }, 1000);
        }
    }
}

function checkWin() {
    const matchedCards = document.querySelectorAll('.matched');
    const totalCards = document.querySelectorAll('.card').length;
    if (matchedCards.length === totalCards) {
        setTimeout(() => {
            alert("Gratulacje! Wygrałeś!"); 
        }, 500);
    }
}
