// Comprueba que app/config.firmado.json (el sobre que leen las apps desde la 1.2.6) tiene una firma válida y lleva
// exactamente la misma configuración que app/config.json (el que leen las versiones anteriores).
// Lo corre el gancho pre-commit: si config.json cambió y no se volvió a firmar, el commit no se hace.
// Para firmar hace falta la llave privada, que no está en este repositorio (se firma desde el proyecto de la app).
// Uso: node herramientas/verificar_config.mjs     Sin dependencias (solo Node).
import { createPublicKey, verify } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { isDeepStrictEqual } from 'node:util';

// Llave pública (no es un secreto): la misma que llevan las apps.
const LLAVE_PUBLICA_BASE64 = 'WiGLS+rA0KvW0mxMQJS4GsG0pkzzyCPa7Uds1XYeGGM=';
const raiz = new URL('../app/', import.meta.url);

function fallo(mensaje) {
  console.error(`verificar_config: ${mensaje}`);
  process.exit(1);
}

try {
  const config = JSON.parse(readFileSync(new URL('config.json', raiz), 'utf8'));
  if (!Number.isInteger(config.serie) || config.serie < 1) fallo('config.json necesita "serie" (entero desde 1) y subirla en cada cambio');
  const sobre = JSON.parse(readFileSync(new URL('config.firmado.json', raiz), 'utf8'));
  const contenido = Buffer.from(sobre.config, 'base64');
  const firma = Buffer.from(sobre.firma, 'base64');
  const spki = Buffer.concat([Buffer.from('302a300506032b6570032100', 'hex'), Buffer.from(LLAVE_PUBLICA_BASE64, 'base64')]);
  const publica = createPublicKey({ key: spki, format: 'der', type: 'spki' });
  if (firma.length !== 64 || !verify(null, contenido, publica, firma)) fallo('la firma de app/config.firmado.json no es válida');
  if (!isDeepStrictEqual(JSON.parse(contenido.toString('utf8')), config)) {
    fallo('app/config.json cambió y app/config.firmado.json no: sube "serie" y vuelve a firmar antes de publicar');
  }
  console.log(`verificar_config: OK (serie ${config.serie})`);
} catch (e) {
  fallo(e.code ?? e.message);
}
