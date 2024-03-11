const scrollToTop = ()=>{
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
}

window.addEventListener('scroll', ()=>{
    var scroll = document.querySelector('.upward')
    scroll.classList.toggle('active', window.scrollY>500);
})

let offset = 0;
const BenefitsBlock = document.querySelector('.BenefitsBlock').offsetWidth;
const SliderLine = document.querySelector('.BenefitsList');

document.querySelector('.btn-right').addEventListener('click', ()=>{
    if (offset - BenefitsBlock >= -BenefitsBlock*5) {
        offset = offset - BenefitsBlock - 10;
        SliderLine.style.left = offset + 'px';   
    }
})
document.querySelector('.btn-left').addEventListener('click', ()=>{
    if (offset + BenefitsBlock <= 0) {
        offset = offset + BenefitsBlock + 10;
        SliderLine.style.left = offset + 'px';   
    }
})
