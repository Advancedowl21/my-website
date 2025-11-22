// Theme toggle + persistence
const toggle = document.getElementById('theme-toggle');
const root = document.documentElement;
const KEY = 'my-website-theme';

function setTheme(mode){
  if(mode === 'dark'){
    document.documentElement.setAttribute('data-theme','dark');
    toggle.textContent = '☀️';
  } else {
    document.documentElement.removeAttribute('data-theme');
    toggle.textContent = '🌙';
  }
  localStorage.setItem(KEY, mode);
}

toggle.addEventListener('click', () => {
  const current = localStorage.getItem(KEY) === 'dark' ? 'dark' : 'light';
  setTheme(current === 'dark' ? 'light' : 'dark');
});

// initialize
const saved = localStorage.getItem(KEY);
if(saved){
  setTheme(saved);
} else {
  // prefer system
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  setTheme(prefersDark ? 'dark' : 'light');
}

// set year
document.getElementById('year').textContent = new Date().getFullYear();

// service worker registration
if('serviceWorker' in navigator){
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(()=>{/*ignore*/});
  });
}
