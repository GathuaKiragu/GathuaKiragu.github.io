const toggle = document.querySelector('.menu-toggle');
const navigation = document.getElementById('navigation');
toggle.hidden = false;
function closeMenu() {
    navigation.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
}
toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    navigation.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
});
navigation.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
});
document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        toggle.focus();
    }
});
window.matchMedia('(min-width: 801px)').addEventListener('change', closeMenu);
document.getElementById('year').textContent = new Date().getFullYear();
// Keep navigation usable when JavaScript is disabled; collapse only after setup.
document.documentElement.classList.add('js');
