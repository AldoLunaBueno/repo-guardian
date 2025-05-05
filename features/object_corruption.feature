# language: es

Característica: Detección de blobs corruptos en packfiles

  Escenario: Blob dañado en packfile
    Dado un repositorio con packfile "fixtures/pack-corrupt.git"
    Cuando ejecuto "guardian scan fixtures/pack-corrupt.git"
    Entonces el exit code es 2
    Y la salida contiene "Invalid CRC at offset"