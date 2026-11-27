// Tema de la portada: oscuro por defecto; claro solo si la persona lo eligió con el botón de la barra (app.js lo guarda).
// Va en el <head> sin defer para aplicarse antes de pintar: así no hay destello del tema equivocado.
try { if (localStorage.getItem('mando-tema') === 'claro') document.documentElement.dataset.tema = 'claro'; } catch (e) {}
