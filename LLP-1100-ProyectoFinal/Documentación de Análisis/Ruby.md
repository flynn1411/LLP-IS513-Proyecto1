# Investigación sobre Ruby

## Sobre Ruby

Ruby es un lenguaje de programación orientado a objetos y multiprpósito. Contiene una sintáxis más natural 
a la de otros lenguajes como C/C++ ó Java. Su implementación es a través de interpretación, por lo que 
su ejecución puede ser lenta en comparación a lenguajes compilados. Su uso se destaca en la web, donde se puede trabajar en Front-End o Back-End; no obstante, es capáz de ser utilizado en aplicaciones de escritorio utilizando librerías como GTK u OpenGL.

## Gramática

### Comentarios:

#### Un comentario simple, o de una línea:

Estos comentarios comienzan con un símbolo de numeral (#), y terminan con un salto
de línea (\n). Lo que sea que se encuentre entre estos dos carácteres es aceptado.
E.G.

```ruby
#Este es un comentario simple en Ruby
a = 5
```

#### Comentarios de múltiples lineas:

Estos comentarios se pueden escribir en una o más lineas, Su comienzo se define con "=begin" y su final con "=end". E.G.

```ruby
=begin
Este es un comentario de multiples 
lineas.
1,2,
3
=end
factorial(6)
```

#### Tipos de Datos:

Según las especificaciones del proyecto, se aceptan:

- ##### Cadenas:
