#  The Veblen Series: Numbers
Veblen Series products are rare non-fungible Tokens (NFTs) that represent 
scarce [Veblen goods](https://en.wikipedia.org/wiki/Veblen_good). Our initial
series consists of algorithmically generated images representing 1000 numbers 
(the integers from 0 to 999), which are unique NFTs tracked on the Polygon
blockchain. These exquisite Veblen Series products can be [viewed and purchased 
on OpenSea](https://opensea.io/collection/veblen-numbers).

# Who was Veblen?
[Thorstein Veblen](https://en.wikipedia.org/wiki/Thorstein_Veblen)
was an influential economist who lived from 1857 to 1929. He is best known
for his work on conspicuous consumption: the purchasing of luxury goods for
[social signaling](https://www.umass.edu/preferen/gintis/moral%20sentiments.pdf#page=127) 
rather than strict consumption. In honor of his work and lasting legacy, we, 
the creators, will donate one-quarter of sales revenue, including our share of
secondary and subsequent sales, to non-profit universities or organizations
conducting fundamental scientific research on social signaling or complexity
economics.

# Who are we?
We are social scientists interested in the social and theoretical aspects
of NFTs. Veblen Series collections, such as these Veblen Numbers, are
meant to provoke awareness and discussion of the roles signaling plays in
the appreciation, consumption, and valuation of art, NFTs, and digital assets.

Find us on Twitter: @TheVeblenSeries

# Art generation
Details on the art generation are available in the comments for the Python
script we used to create the images. While doing so does not provide ownership
of the associated art, to generate them yourself, simply clone this repository, 
change directory into it, and run the Python script make_veblen_numbers.py. 
This requires that the python packages PIL and numpy are installed and that 
the DejaVuSans font is available. Once these requirements are met, generate
the images with the following commands:

```bash
git clone https://github.com/MichaelHoltonPrice/p3k_baydem
cd p3k_baydem
python3 make_veblen_numbers.py
```