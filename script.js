let linksRevealed = false;

function revealLinks() {
    if (!linksRevealed) {
        const linksSection = document.getElementById('linksSection');
        linksSection.classList.remove('hidden');
        linksSection.classList.add('fade-in');
        linksRevealed = true;
    }
}

// -- PETTING LOGIC --
function petRabbitAnimation() {
    const rabbit = document.getElementById('rabbit');
    const heart = document.getElementById('heart');
    const hand = document.getElementById('animatedHand');
    
    // El animasyonu başlar
    hand.classList.remove('hidden');
    hand.classList.add('pat-animation');

    // Tavşan tepki verir: gözler kapanır, kulaklar iner
    rabbit.classList.add('petting');
    
    setTimeout(() => {
        // Kalp çıkar
        heart.classList.remove('hidden');
        heart.style.animation = 'none';
        void heart.offsetWidth; // reflow
        heart.style.animation = 'floatUp 1s ease-out forwards';
    }, 600);

    // Animasyon sonrası eski haline dön
    setTimeout(() => {
        hand.classList.add('hidden');
        hand.classList.remove('pat-animation');
        rabbit.classList.remove('petting');
        revealLinks();
    }, 2000);
}

// -- DRAG AND DROP RABBIT FEEDING LOGIC --
const rabbitDropZone = document.getElementById('rabbit');
const carrot = document.getElementById('draggableCarrot');

// Sürükleme başladığında
carrot.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', 'carrot');
    carrot.classList.add('dragging');
    setTimeout(() => { carrot.style.opacity = '0.5'; }, 0);
});

// Sürükleme bittiğinde
carrot.addEventListener('dragend', () => {
    carrot.classList.remove('dragging');
    carrot.style.opacity = '1';
});

// Tavşanın üzerine gelindiğinde
rabbitDropZone.addEventListener('dragover', (e) => {
    e.preventDefault(); // Bırakmaya izin ver
});

// Tavşanın üzerine bırakıldığında
rabbitDropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    const data = e.dataTransfer.getData('text/plain');
    if (data === 'carrot') {
        eatCarrot();
    }
});

function eatCarrot() {
    const rabbit = document.getElementById('rabbit');
    const crumbs = document.getElementById('eating-crumbs');
    
    // Havucu gizle (yendiği için)
    carrot.style.visibility = 'hidden';
    
    // Tavşan mutlu şekilde yer
    rabbit.classList.add('eating');
    crumbs.classList.remove('hidden');
    
    // Yeme animasyonu bitişi
    setTimeout(() => {
        rabbit.classList.remove('eating');
        crumbs.classList.add('hidden');
        revealLinks();
        
        // Bir süre sonra havucu geri getir
        setTimeout(() => { carrot.style.visibility = 'visible'; }, 2000);
    }, 2500);
}
