#!/bin/zsh
bundler install
asciidoctor-pdf -r asciidoctor-diagram -r asciidoctor-lists -v --theme theme/daw-theme.yml -a toc index.adoc
asciidoctor-pdf -v --theme theme/daw-theme-cover.yml -a pdf-fontsdir=theme/fonts includes/preface.adoc
ruby scripts/combine_pdf.rb
rm index.pdf
rm includes/preface.pdf
