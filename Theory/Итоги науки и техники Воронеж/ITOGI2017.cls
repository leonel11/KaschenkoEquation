%%
%% This is file `amsart.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% amsclass.dtx  (with options: `amsart')

%%% ====================================================================
%%%  @LaTeX-file{
%%%     filename        = "amsclass.dtx",
%%%     version         = "1.2b",
%%%     date            = "1995/02/23",
%%%     time            = "10:06:48 EST",
%%%     author          = "American Mathematical Society",
%%%     copyright       = "Copyright (C) 1995 American Mathematical Society,
%%%                        all rights reserved.  Copying of this file is
%%%                        authorized only if either:
%%%                        (1) you make absolutely no changes to your copy,
%%%                        including name; OR
%%%                        (2) if you do make changes, you first rename it
%%%                        to some other name.",
%%%     address         = "American Mathematical Society,
%%%                        Technical Support,
%%%                        Electronic Products and Services,
%%%                        P. O. Box 6248,
%%%                        Providence, RI 02940,
%%%                        USA",
%%%     telephone       = "401-455-4080 or (in the USA and Canada)
%%%                        800-321-4AMS (321-4267)",
%%%     FAX             = "401-331-3842",
%%%     checksum        = "06446 3073 12220 114673",
%%%     email           = "tech-support@math.ams.org (Internet)",
%%%     codetable       = "ISO/ASCII",
%%%     keywords        = "latex, amslatex, ams-latex",
%%%     supported       = "yes",
%%%     abstract        = "This is part of the AMS-\LaTeX{} distribution.
%%%                        It produces output conforming to the style
%%%                        conventions of American Mathematical Society
%%%                        publications.  The file \fn{amsclass.dtx} is
%%%                        converted by the installation procedure
%%%                        into three document classes:
%%%                        \cls{amsart}, \cls{amsproc}, and \cls{amsbook},
%%%                        which are intended, respectively,
%%%                        for articles and books containing mathematical
%%%                        research; both class files will also carry this
%%%                        heading, and the particular class should be
%%%                        determined from the external file name.",
%%%     docstring       = "The checksum field above contains a CRC-16
%%%                        checksum as the first value, followed by the
%%%                        equivalent of the standard UNIX wc (word
%%%                        count) utility output of lines, words, and
%%%                        characters.  This is produced by Robert
%%%                        Solovay's checksum utility.",
%%%  }
%%% ====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cmiar}[1995/02/23 v1.2b]
\def\@tempa#1#2\@nil{\edef\@classname{#1}}
\expandafter\@tempa\@currnamestack{}{}{}\@nil
\ifx\@classname\@empty \edef\@classname{\@currname}\fi


\DeclareOption{vinitilogo}{\def\VNL{\includegraphics[width=20mm]{viniti.eps}}}
\def\VNL{\relax}

\DeclareOption{a4paper}{\paperheight 297mm\paperwidth 210mm}
\DeclareOption{letterpaper}{\paperheight 11in\paperwidth 8.5in}
\DeclareOption{landscape}{\@tempdima\paperheight
  \paperheight\paperwidth \paperwidth\@tempdima}
\DeclareOption{portrait}{}
\DeclareOption{oneside}{\@twosidefalse \@mparswitchfalse}
\DeclareOption{twoside}{\@twosidetrue  \@mparswitchtrue}
\DeclareOption{draft}{\overfullrule5\p@ }
\DeclareOption{final}{\overfullrule\z@ }
\newif\if@titlepage
\DeclareOption{titlepage}{\@titlepagetrue}
\DeclareOption{notitlepage}{\@titlepagefalse}
\DeclareOption{onecolumn}{\@twocolumnfalse}
\DeclareOption{twocolumn}{\@twocolumntrue}
\DeclareOption{nomath}{%
  \def\numberwithin##1##2{\@ifundefined{c@##1}{\@nocounterr{##1}}{%
    \@ifundefined{c@##2}{\@nocounterr{##2}}{%
    \@addtoreset{##1}{##2}%
    \toks@\@xp\@xp\@xp{\csname the##1\endcsname}%
    \@xp\xdef\csname the##1\endcsname
      {\@xp\@nx\csname the##2\endcsname
       .\the\toks@}}}}
}
\def\mathfrak{needed}
\DeclareOption{noamsfonts}{\let\mathfrak\relax}
\DeclareOption{psamsfonts}{%
  \PassOptionsToPackage{psamsfonts}{amsfonts}%
  \PassOptionsToPackage{cmex10}{amsmath}}
\newif\iftagsleft@
\DeclareOption{leqno}{%
  \tagsleft@true \PassOptionsToPackage{leqno}{amsmath}}
\DeclareOption{reqno}{%
  \tagsleft@false \PassOptionsToPackage{reqno}{amsmath}}
\newif\ifctagsplit@
\DeclareOption{centertags}{%
  \ctagsplit@true \PassOptionsToPackage{centertags}{amsmath}}
\DeclareOption{tbtags}{%
  \ctagsplit@false \PassOptionsToPackage{tbtags}{amsmath}}
\DeclareOption{fleqn}{%
  \def\[{\relax
    \ifmmode\@badmath
    \else
      \begin{trivlist}%
      \@beginparpenalty\predisplaypenalty
      \@endparpenalty\postdisplaypenalty
      \item[]\leavevmode
      \hbox to\linewidth\bgroup$\displaystyle
      \hskip\mathindent\bgroup
    \fi}%
  \def\]{\relax
    \ifmmode
      \egroup \m@th$\hfil \egroup
      \end{trivlist}%
    \else \@badmath
    \fi}%
  \renewenvironment{equation}{%
    \@beginparpenalty\predisplaypenalty
    \@endparpenalty\postdisplaypenalty
    \refstepcounter{equation}%
    \@topsep\abovedisplayskip \trivlist
    \item[]\leavevmode
    \hbox to\linewidth\bgroup\hskip\mathindent$\displaystyle
  }{%
    \m@th$\hfil \displaywidth\linewidth \hbox{\@eqnnum}\egroup
    \endtrivlist
  }%
  \renewenvironment{eqnarray}{%
    \stepcounter{equation}\let\@currentlabel\theequation
    \global\@eqnswtrue \global\@eqcnt\z@ \tabskip\mathindent
    \let\\=\@eqncr \abovedisplayskip\topsep
    \ifvmode \advance\abovedisplayskip\partopsep \fi
    \belowdisplayskip\abovedisplayskip
    \belowdisplayshortskip\abovedisplayskip
    \abovedisplayshortskip\abovedisplayskip
    $$\everycr{}\halign to\linewidth\bgroup
      \hskip\@centering
      $\displaystyle\tabskip\z@skip####\m@th$&%
      \@eqnsel \global\@eqcnt\@ne
      \hfil${}####{}\m@th$\hfil&%
      \global\@eqcnt\tw@
      $\displaystyle ####\m@th$\hfil\tabskip\@centering&%
      \global\@eqcnt\thr@@
      \hbox to \z@\bgroup\hss####\egroup\tabskip\z@skip\cr
    }{%
      \@@eqncr \egroup \global\advance\c@equation\m@ne$$%
      \global\@ignoretrue
    }%
  \newdimen\mathindent \mathindent\leftmargini
}
\newcommand{\@mainsize}{10}
\newcommand{\@ptsize}{0}
\newcommand{\larger}[1][1]{%
  \count@\@currsizeindex \advance\count@#1\relax
  \ifnum\count@<\z@ \count@\z@ \else\ifnum\count@>12 \count@12 \fi\fi
  \ifcase\count@
    \Tiny\or\Tiny\or\tiny\or\SMALL\or\Small\or\small
    \or\normalsize
    \or\large\or\Large\or\LARGE\or\huge\or\Huge\else\Huge
  \fi
}
\newcommand{\smaller}[1][1]{\larger[-#1]}
\def\@adjustvertspacing{%
  \bigskipamount.7\baselineskip plus.7\baselineskip
  \medskipamount\bigskipamount \divide\medskipamount\tw@
  \smallskipamount\medskipamount \divide\smallskipamount\tw@
  \abovedisplayskip\medskipamount
  \belowdisplayskip \abovedisplayskip
  \abovedisplayshortskip\abovedisplayskip
  \advance\abovedisplayshortskip-1\abovedisplayskip
  \belowdisplayshortskip\abovedisplayshortskip
  \advance\belowdisplayshortskip 1\smallskipamount
  \jot\baselineskip \divide\jot 4 \relax
}
\renewcommand\normalsize{\@xsetfontsize\normalsize 6%
  \@adjustvertspacing \let\@listi\@listI}
\newcommand\Tiny{\@xsetfontsize\Tiny 1}
\newcommand\tiny{\@xsetfontsize\tiny 2}
\newcommand\SMALL{\@xsetfontsize\SMALL 3}
\newcommand\Small{\@xsetfontsize\Small 4%
  \@adjustvertspacing
  \def\@listi{\topsep\smallskipamount \parsep\z@skip \itemsep\z@skip}}
\newcommand\small{\@xsetfontsize\small 5\@adjustvertspacing}
\def\footnotesize{\Small}
\def\scriptsize{\SMALL}
\newcommand\large{\@xsetfontsize\large 7\@adjustvertspacing}
\newcommand\Large{\@xsetfontsize\Large 8\@adjustvertspacing}
\newcommand\LARGE{\@xsetfontsize\LARGE 9}
\newcommand\huge{\@xsetfontsize\huge{10}}
\newcommand\Huge{\@xsetfontsize\Huge{11}}
\def\@xsetfontsize#1#2{%
  \chardef\@currsizeindex#2\relax
  \edef\@tempa{\@nx\@setfontsize\@nx#1%
    \@xp\ifcase\@xp\@currsizeindex\@typesizes
      \else{99}{99}\fi}%
  \@tempa
}
\chardef\@currsizeindex=6
\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000
\newdimen\linespacing
\lineskip=1pt \lineskiplimit=1pt
\normallineskip=1pt \normallineskiplimit=1pt
\let\baselinestretch=\@empty
\headheight=7pt
\headsep=20pt
\footskip=30pt
\topskip=10pt
\textheight=250mm
\textwidth=170mm
\columnsep=10pt \columnseprule=0pt
\marginparwidth=90pt
\marginparsep=11pt
\marginparpush=5pt
\AtBeginDocument{\settoheight{\footnotesep}{\footnotesize M$^1$}}
\skip\footins=7pt plus11pt
\skip\@mpfootins=\skip\footins
\fboxsep=3pt \fboxrule=.4pt
\arrayrulewidth=.4pt    \doublerulesep=2pt
\labelsep=5pt           \arraycolsep=\labelsep
\tabcolsep=\labelsep    \tabbingsep=\labelsep
\floatsep=15pt plus 12pt    \dblfloatsep=15pt plus 12pt
\textfloatsep=\floatsep  \dbltextfloatsep=15pt plus 12pt
\intextsep=\floatsep
\@fptop=0pt plus1fil     \@dblfptop=0pt plus1fil
\@fpbot=0pt plus1fil     \@dblfpbot=0pt plus1fil
\@fpsep=8pt plus2fil     \@dblfpsep=8pt plus2fil\relax
\parskip=0pt \relax
\newdimen\normalparindent
\normalparindent=12pt
\parindent=\normalparindent
\partopsep=0pt \relax \parsep=0pt \relax \itemsep=0pt \relax
\@lowpenalty=51         \@medpenalty=151        \@highpenalty=301
\@beginparpenalty=-\@lowpenalty
\@endparpenalty=-\@lowpenalty
\@itempenalty=-\@lowpenalty
\DeclareOption{10pt}{\def\@mainsize{10}\def\@ptsize{0}%
  \def\@typesizes{%
    \or{5}{6}\or{6}{7}\or{7}{8}\or{8}{10}\or{9}{11}%
    \or{10}{12}% normalsize
    \or{\@xipt}{13}\or{\@xiipt}{14}\or{\@xivpt}{17}%
    \or{\@xviipt}{20}\or{\@xxpt}{24}}%
  \normalsize \linespacing=\baselineskip
}
\DeclareOption{11pt}{\def\@mainsize{11}\def\@ptsize{1}%
  \def\@typesizes{%
    \or{6}{7}\or{7}{8}\or{8}{10}\or{9}{11}\or{10}{12}%
    \or{\@xipt}{13}% normalsize
    \or{\@xiipt}{14}\or{\@xivpt}{17}\or{\@xviipt}{20}%
    \or{\@xxpt}{24}\or{\@xxvpt}{30}}%
  \normalsize \linespacing=\baselineskip
}
\DeclareOption{12pt}{\def\@mainsize{12}\def\@ptsize{2}%
  \def\@typesizes{%
    \or{7}{8}\or{8}{10}\or{9}{11}\or{10}{12}\or{\@xipt}{13}%
    \or{\@xiipt}{14}% normalsize
    \or{\@xivpt}{17}\or{\@xviipt}{20}\or{\@xxpt}{24}%
    \or{\@xxvpt}{30}\or{\@xxvpt}{30}}%
  \normalsize \linespacing=\baselineskip
}
\DeclareOption{8pt}{\def\@mainsize{8}\def\@ptsize{8}%
  \def\@typesizes{%
    \or{5}{6}\or{5}{6}\or{5}{6}\or{6}{7}\or{7}{8}%
    \or{8}{10}% normalsize
    \or{9}{11}\or{10}{12}\or{\@xipt}{13}%
    \or{\@xiipt}{14}\or{\@xivpt}{17}}%
  \normalsize \linespacing=\baselineskip
}
\DeclareOption{9pt}{\def\@mainsize{9}\def\@ptsize{9}%
  \def\@typesizes{%
    \or{5}{6}\or{5}{6}\or{6}{7}\or{7}{8}\or{8}{10}%
    \or{9}{11}% normalsize
    \or{10}{12}\or{\@xipt}{13}\or{\@xiipt}{14}%
    \or{\@xivpt}{17}\or{\@xviipt}{20}}%
  \normalsize \linespacing=\baselineskip
}
\def\ps@empty{\let\@mkboth\@gobbletwo
  \let\@oddhead\@empty \let\@evenhead\@empty
  \let\@oddfoot\@empty \let\@evenfoot\@empty
  \global\topskip\normaltopskip}
\def\ps@plain{\ps@empty
  \def\@oddfoot{\normalfont\scriptsize \hfil\thepage\hfil}%
  \let\@evenfoot\@oddfoot}
\def\ps@headings{\ps@empty
  \def\@evenhead{\normalfont\scriptsize
      \rlap{\thepage}\hfil \leftmark{}{}\hfil}%
  \def\@oddhead{\normalfont\scriptsize \hfil
      \rightmark{}{}\hfil \llap{\thepage}}
%   \def\@evenfoot{\hfil\normalfont\scriptsize Ñîâðåìåííàÿ ìàòåìàòèêà è åå ïðèëîæåíèÿ.
%   \@currentyear\ ã. Ò. \@currentvolume\hfil}
    \def\@evenfoot{\relax}
   \let\@oddfoot\@evenfoot

  \let\@mkboth\markboth
}
\let\sectionname\@empty
\let\subsectionname\@empty
\let\subsubsectionname\@empty
\def\leftmark{\expandafter\@firstoftwo\topmark{}{}}
\def\rightmark{\expandafter\@secondoftwo\botmark{}{}}
%\def\ps@firstpage{\ps@plain
%  \def\@oddfoot{\normalfont\scriptsize \hfil\thepage\hfil
%     \global\topskip\normaltopskip
%     }%
%  \let\@evenfoot\@oddfoot
%  \def\@oddhead{\serieslogo@\hss}%
%  \let\@evenhead\@oddhead}% in case an article starts on a left-hand page
\def\@setfirstpage{ISSN \ISSN\quad\copyright\
     ÂÈÍÈÒÈ ÐÀÍ, \@currentyear}
\def\ps@firstpage{\ps@plain
  \def\@oddfoot{\normalfont\scriptsize \hfil\@setfirstpage\hfil
     \global\topskip\normaltopskip
     }%
  \let\@evenfoot\@oddfoot
  \def\@oddhead{\serieslogo@\hss}%
  \let\@evenhead\@oddhead}% in case an article starts on a left-hand page
\long\def\@nilgobble#1\@nil{}
\def\markboth#1#2{%
  \begingroup
    \@temptokena{{#1}{#2}}\xdef\@themark{\the\@temptokena}%
    \mark{\the\@temptokena}%
  \endgroup
  \if@nobreak\ifvmode\nobreak\fi\fi}
\def\ps@myheadings{\ps@headings \let\@mkboth\@gobbletwo}
\newskip\normaltopskip
\normaltopskip=10pt \relax

\let\partmark\@gobble
\let\chaptermark\@gobble
\let\sectionmark\@gobble
\let\subsectionmark\@gobble
\let\subsubsectionmark\@gobble
\let\paragraphmark\@gobble

\input{ifthen.sty}

\DeclareOption{makeidx}{}
\input{amsgen.sty}
\ExecuteOptions{reqno,centertags,a4paper,portrait,11pt,twoside,onecolumn,final}
\ProcessOptions\relax
\if@compatibility
  \def\@tempa#1{\let\mathfrak\relax
    \RequirePackage{amstex}\relax}\expandafter\@tempa
\else
  \expandafter\@iden
\fi
{% if native mode
\@ifundefined{numberwithin}{\let\@tempa\relax}{\let\@tempa\@gobbletwo}
\@tempa
\RequirePackage{amsmath}\relax
%\RequirePackage{onlyamsmath}\relax
\ifx\relax\mathfrak \@xp\@gobbletwo \else \let\mathfrak\relax \fi
\RequirePackage{amsfonts}\relax
}% end native mode branch
\newcommand{\uppercasenonmath}[1]{\toks@\@emptytoks
  \@xp\@skipmath\@xp\@empty#1$$%
  \edef#1{\@nx\@upprep\the\toks@}%
}
\newcommand{\@upprep}{%
  \spaceskip1.3\fontdimen2\font plus1.3\fontdimen3\font
  \upchars@}
\newcommand{\upchars@}{%
  \def\ss{SS}\def\i{I}\def\j{J}\def\ae{\AE}\def\oe{\OE}%
  \def\o{\O}\def\aa{\AA}\def\l{\L}\def\Mc{M{\scshape c}}}
\newcommand{\@skipmath}{}
\long\def\@skipmath#1$#2${%
  \@xskipmath#1\(\)%
  \@ifnotempty{#2}{\toks@\@xp{\the\toks@$#2$}\@skipmath\@empty}}%
\newcommand{\@xskipmath}{}
\long\def\@xskipmath#1\(#2\){%
  \uppercase{\toks@\@xp\@xp\@xp{\@xp\the\@xp\toks@#1}}%
  \@ifnotempty{#2}{\toks@\@xp{\the\toks@\(#2\)}\@xskipmath\@empty}}%
\newcommand{\today}{%
  \relax\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\renewcommand{\title}[2][]{\gdef\shorttitle{#1}\gdef\@title{#2}}

\newcounter{num@auth}
\setcounter{num@auth}{0}

\gdef\forlastauthors{\relax}

\edef\title{\@nx\@dblarg
  \@xp\@nx\csname\string\title\endcsname}
\renewcommand{\author}[2][]{%
  \ifx\@empty\authors
    \gdef\firstshortauthors{#1}
    \gdef\shortauthors{#2}
    \gdef\firstshortauthor{#1}%
    \gdef\firstauthor{#2}%
    \gdef\authors{#2}%
  \else
    \g@addto@macro\firstshortauthors{\and#1}%
    \g@addto@macro\addresses{\forlastauthors{#1}}%
    \g@addto@macro\shortauthors{\and#2}%
    \g@addto@macro\authors{\and#2}%
  \fi
  \g@addto@macro\addresses{\author{}}%
  \global\refstepcounter{num@auth}
}
\edef\author{\@nx\@dblarg
  \@xp\@nx\csname\string\author\endcsname}
\let\shortauthors\@empty   \let\authors\@empty
\let\addresses\@empty      \let\thankses\@empty
\newcommand{\address}[2][]{\g@addto@macro\addresses{\address{#1}{#2}}}
\newcommand{\curraddr}[2][]{\g@addto@macro\addresses{\curraddr{#1}{#2}}}
\newcommand{\email}[2][]{\g@addto@macro\addresses{\email{#1}{#2}}}
\renewcommand{\thanks}[1]{\g@addto@macro\thankses{\thanks{#1}}}
\def\enddoc@text{
  \bigskip
  \ifx\@empty\@translators \else\@settranslators\fi
  \ifx\@empty\addresses \else
    \begingroup
    \ifnum\value{num@auth}>1
    \par
       \ifx\@empty\firstshortauthor \firstauthor \else \firstshortauthor\fi
     \else
       \ifx\@empty\firstshortauthor\else \firstshortauthor\fi
    \fi
    \endgroup
  \@setaddresses\fi}
\AtEndDocument{\enddoc@text}
\def\@setaddresses{\par
  \nobreak \begingroup
%\footnotesize
  \def\\{\par}%
            \ifx\@empty\firstshortauthors\else
            \forlastauthors
            \fi
      \interlinepenalty\@M
       \def\firstshortauthors##1{\begingroup
       \par\addvspace\bigskipamount\indent
       {\upshape\ignorespaces##1}\par\endgroup}% %% AO
%%
  \def\address##1##2{\begingroup
    \par%\addvspace\bigskipamount
    \indent
   \@ifnotempty{##1}{(\ignorespaces##1\unskip) }%
    {\upshape\ignorespaces##2}\par\endgroup}% %% AO
%
  \def\curraddr##1##2{\begingroup
    \@ifnotempty{##2}{\nobreak\indent{\itshape Current address}%
      \@ifnotempty{##1}{, \ignorespaces##1\unskip}\/:\space
      ##2\par\endgroup}}%
  \def\email##1##2{\begingroup
    \@ifnotempty{##2}{\nobreak\indent{E-mail}%
      \@ifnotempty{##1}{, \ignorespaces##1\unskip}\/:\space
      \ttfamily##2\par
      \endgroup}\medskip}%
  \addresses
  \endgroup
}
\let\@date\@empty
\def\dedicatory#1{\def\@dedicatory{#1}}
\let\@dedicatory=\@empty
\def\keywords#1{\def\@keywords{#1}}
\def\@keywords{{\bfseries \LARGE ÇÀÏÎËÍÈÒÅ ÏÎËÅ!!!}}
\newcommand*\subjclass[2][1991]{%
  \def\@subjclass{#2}%
  \@ifundefined{subjclassname@#1}{%
    \ClassWarning{\@classname}{Unknown edition (#1) of Mathematics
      Subject Classification; using '1991'.}%
  }{%
    \@xp\let\@xp\subjclassname\csname subjclassname@#1\endcsname
  }%
}
\def\UDC#1{\def\@UDC{#1}}
\def\@subjclass{{\bfseries \LARGE ÇÀÏÎËÍÈÒÅ ÏÎËÅ!!!}}
\def\@UDC{{\bfseries \LARGE ÇÀÏÎËÍÈÒÅ ÏÎËÅ!!!}}
\def\commby#1{\def\@commby{(Communicated by #1)}}
\let\@commby=\@empty
\def\translator#1{\g@addto@macro\@translators{\and#1}}
\let\@translators=\@empty
\def\@settranslators{\par\begingroup
  \addvspace{6\p@\@plus9\p@}%
  \hbox to\columnwidth{\hss\normalfont\normalsize
    Translated by %
    \andify\@translators \uppercasenonmath\@translators
    \@translators}
  \endgroup
}
\newcommand{\xandlist}[4]{\@andlista{{#1}{#2}{#3}}#4\and\and}
\def\@andlista#1#2\and#3\and{\@andlistc{#2}\@ifnotempty{#3}{%
  \@andlistb#1{#3}}}
\def\@andlistb#1#2#3#4#5\and{%
  \@ifempty{#5}{%
    \@andlistc{#2#4}%
  }{%
    \@andlistc{#1#4}\@andlistb{#1}{#3}{#3}{#5}%
  }}
\let\@andlistc\@iden
\newcommand{\nxandlist}[4]{%
  \def\@andlistc##1{\toks@\@xp{\the\toks@##1}}%
  \toks@{\toks@\@emptytoks \@andlista{{#1}{#2}{#3}}}%
  \the\@xp\toks@#4\and\and
  \edef#4{\the\toks@}%
  \let\@andlistc\@iden}
\newcommand{\andify}{%
  \nxandlist{\unskip, }{\unskip, }{\unskip, }}
\def\and{\unskip{ }and \ignorespaces}
\def\maketitle{\par
  \@topnum\z@ % this prevents figures from falling at the top of page 1
%  \@setcopyright
  \ifx\@empty\@UDC
%  {\hfill\UDCname\enspace {\bfseries \LARGE ÇÀÏÎËÍÈÒÅ ÏÎËÅ!!!}\par\bigskip}
  \else
  \vspace*{1cm}
  {\hfill\UDCname\enspace\@UDC\par\bigskip}\fi
%  \vspace*{1mm}
  \uppercasenonmath\shorttitle
  \uppercasenonmath\firstauthor
  \ifx\@empty\shortauthors \let\shortauthors\shorttitle
  \else \andify\shortauthors \uppercasenonmath\shortauthors \fi
  \begingroup
  \@maketitle
  \ifnum\value{num@auth}>3
    \toks@\@xp{\firstauthor \ è äð.}
    \else
    \toks@\@xp{\shortauthors}
  \fi
  \@temptokena\@xp{\shorttitle}%
  \edef\@tempa{\@nx
  \markboth{\the\toks@}{\the\@temptokena}
  }\@tempa
  \endgroup
\thispagestyle{firstpage}% this sets first page specifications
  \c@footnote\z@
  \def\do##1{\let##1\relax}%
  \do\maketitle \do\@maketitle \do\title \do\@xtitle \do\@title
  \do\author \do\@xauthor \do\address \do\@xaddress
  \do\email \do\@xemail \do\curraddr \do\@xcurraddr
\do\commby \do\@commby
  \do\dedicatory \do\@dedicatory \do\thanks \do\thankses
  \do\keywords \do\@keywords \do\subjclass \do\@subjclass
}
\def\@maketitle{%
  \normalfont\normalsize
  \let\@makefnmark\relax  \let\@thefnmark\relax
  \ifx\@empty\@date\else \@footnotetext{\@setdate}\fi
%  \ifx\@empty\@keywords\else \@footnotetext{\@setkeywords}\fi
  \ifx\@empty\thankses\else \@footnotetext{%
    \def\par{\let\par\@par}\@setthanks}\fi
  \@mkboth{\@nx\authors}{\@nx\shorttitle}%
  \global\topskip42\p@\relax % 5.5pc   "   "   "     "     "
  \@settitle
  \ifx\@empty\authors \else \@setauthors \fi
  \ifx\@empty\@dedicatory
  \else
    \baselineskip18\p@
    \vtop{\centering{\footnotesize\itshape\@dedicatory\@@par}%
      \global\dimen@i\prevdepth}\prevdepth\dimen@i
  \fi
  \@setabstract
  \normalsize
  \if@titlepage
    \newpage
  \else
    \dimen@34\p@ \advance\dimen@-\baselineskip
    \vskip\dimen@\relax
  \fi
} % end \@maketitle

\def\serieslogo@{\bfseries\sffamily
 \hbox to 25 mm{\VNL}\vbox{ÈÒÎÃÈ ÍÀÓÊÈ È ÒÅÕÍÈÊÈ.
 \\[2mm]
 Ñîâðåìåííàÿ ìàòåìàòèêà è åå ïðèëîæåíèÿ.  \\[1.5mm]
 Òåìàòè÷åñêèå îáçîðû.
 \\[1.5mm]
 Òîì \@currentvolume\ (\@currentyear\unskip).
 Ñ.~\thepage--\pageref{ENDPAGE}}}

\def\copyrightyear{0000}
\def\copyrightyearmodC{56}
\def\ISSN{0233--6723} % ÂÈÍÈÒÈ
\def\copyrightprice{\$1.00\;+\;\$.25 per page}
\def\currentvolume#1{\def\@currentvolume{#1}}
\def\currentyear#1{\def\@currentyear{#1}}
\def\currentissue{90}
\def\currentmonth{Xxxx}
\newinsert\copyins
\skip\copyins=1.5pc
\count\copyins=1000 % magnification factor, 1000 = 100%
\dimen\copyins=.5\textheight % maximum allowed per page
\def\@setcopyright{%
  \ifx\@empty\serieslogo@
  \else
    \insert\copyins{\hsize\textwidth
      \parfillskip\z@ \leftskip\z@\@plus.9\textwidth
      \fontsize{6}{7\p@}\normalfont\upshape
      \everypar{}%
      \vskip-\skip\copyins \nointerlineskip
      \noindent\vrule\@width\z@\@height\skip\copyins
      \copyright\@currentyear\ ÂÈÍÈÒÈ ÐÀÍ\break
      ISSN \ISSN\break
%      \copyrightyearmodC\ \copyrightprice\par
      \kern\z@}%
  \fi
}
\def\@combinefloats{%
  \ifx \@toplist\@empty \else \@cflt \fi
  \ifx \@botlist\@empty \else \@cflb \fi
  \ifvoid\copyins \else \@cflci \fi
}
\def\@cflci{%
  \if\if@twocolumn \if@firstcolumn F\else T\fi\else T\fi T%
      \setbox\@outputbox\vbox{%
        \unvbox\@outputbox
        \vskip\skip\copyins
        \hbox to\columnwidth{%
          \hss\vbox to\z@{\vss\unvbox\copyins}}}%
  \fi
}
\newcommand{\abstractname}{Abstract}
\newcommand{\keywordsname}{Êëþ÷åâûå ñëîâà}
\newcommand{\subjclassname}{AMS Subject Classification}
\newcommand{\UDCname}{ÓÄÊ}
\def\@tempb{amsart}
\ifx\@classname\@tempb
  \newcommand{\datename}{\textit{Date}:}
\else
  \newcommand{\datename}{Received by the editors}
\fi
\def\@settitle{\begin{center}
% ddd  \baselineskip14\p@\relax
    \large\bfseries
  \baselineskip20\p@\relax
\uppercasenonmath\@title
  \@title
  \end{center}%
}
\def\@setauthors{%
  \begingroup
  \trivlist
  \centering\footnotesize \@topsep30\p@\relax
  \advance\@topsep by -\baselineskip
  \item\relax
  \andify\authors
%%% ddd
\large
\uppercasenonmath\authors
{\small\copyright\ \@currentyear\ ã.} \quad
  \bfseries\small\authors
  \endtrivlist
  \endgroup
}
\def\@setdate{\datename\ \@date\@addpunct.}
\def\@setsubjclass{%
  {\bfseries{\itshape\subjclassname}:}\enspace\@subjclass}
%\def\@setUDC{%
%  {\UDCname}\enspace\@UDC}
\def\@setkeywords{%
  {\bfseries{\itshape \keywordsname}:}\enspace \@keywords\@addpunct.}
\def\@setthanks{\def\thanks##1{\par##1\@addpunct.}\thankses}
\newbox\abstractbox
\newenvironment{abstract}{%
  \ifx\maketitle\relax
    \ClassWarning{\@classname}{Abstract should precede
      \protect\maketitle\space in AMS documentclasses; reported}%
  \fi
  \global\setbox\abstractbox=\vtop \bgroup
  \normalfont\footnotesize
  \advance \hsize -6pc
  \trivlist \labelsep.5em\item[\hskip\labelsep
    {\scshape\abstractname}.]\ignorespaces
}{%
 \medskip\par\noindent\@setkeywords
 \medskip\par\noindent\@setsubjclass
  \endtrivlist
  \egroup
  \ifx\@setabstract\relax \@setabstracta \fi
}
\def\@setabstract{\@setabstracta \global\let\@setabstract\relax}
\def\@setabstracta{%
  \ifvoid\abstractbox
  \else
    \skip@20\p@ \advance\skip@-\lastskip
    \advance\skip@-\baselineskip \vskip\skip@
  \moveright 3pc
    \box\abstractbox
  \fi
}
\def\titlepage{%
  \clearpage
  \thispagestyle{empty}\setcounter{page}{0}}
\def\endtitlepage{\newpage}
\def\labelenumi{\theenumi.}
\def\theenumi{\@arabic\c@enumi}
\def\labelenumii{(\theenumii)}
\def\theenumii{\@alph\c@enumii}
\def\p@enumii{\theenumi}
\def\labelenumiii{(\theenumiii)}
\def\theenumiii{\@roman\c@enumiii}
\def\p@enumiii{\theenumi(\theenumii)}
\def\labelenumiv{(\theenumiv)}
\def\theenumiv{\@Alph\c@enumiv}
\def\p@enumiv{\p@enumiii\theenumiii}
\def\labelitemi{$\m@th\bullet$}
\def\labelitemii{\bfseries --}% \upshape already done by \itemize
\def\labelitemiii{$\m@th\ast$}
\def\labelitemiv{$\m@th\cdot$}
\def\verse{\let\\\@centercr
  \list{}{\itemsep\z@ \itemindent -1.5em\listparindent\itemindent
  \rightmargin\leftmargin \advance\leftmargin 1.5em}\item[]}
\let\endverse=\endlist
\def\quotation{\list{}{%
    \leftmargin3pc \listparindent\normalparindent
    \itemindent\z@
    \rightmargin\leftmargin \parsep\z@ \@plus\p@}%
  \item[]}
\let\endquotation=\endlist
\def\quote{\list{}{\rightmargin\leftmargin}\item[]}
\let\endquote=\endlist
\def\trivlist{\parsep\parskip\@nmbrlistfalse
  \@trivlist \labelwidth\z@ \leftmargin\z@
  \itemindent\z@
  \let\@itemlabel\@empty
  \def\makelabel##1{\upshape##1}}

\def\enumerate{\ifnum \@enumdepth >3 \@toodeep\else
      \advance\@enumdepth \@ne
      \edef\@enumctr{enum\romannumeral\the\@enumdepth}\list
      {\csname label\@enumctr\endcsname}{\usecounter
        {\@enumctr}\def\makelabel##1{\hss\llap{\upshape##1}}}\fi}

\def\itemize{%
  \ifnum\@itemdepth>3 \@toodeep
  \else \advance\@itemdepth\@ne
    \edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
    \list{\csname\@itemitem\endcsname}%
      {\def\makelabel##1{\hss\llap{\upshape##1}}}%
  \fi}
\newcommand{\descriptionlabel}[1]{\hspace\labelsep \upshape\bfseries #1:}
\newcommand{\description}{\list{}{%
  \advance\leftmargini6\p@ \itemindent-12\p@
  \labelwidth\z@ \let\makelabel\descriptionlabel}}
\let\enddescription=\endlist
\let\upn=\textup
\AtBeginDocument{%
  \settowidth\leftmargini{\labelenumi\hskip\labelsep}%
  \advance\leftmargini by \normalparindent
  \settowidth\leftmarginii{\labelenumii\hskip\labelsep}%
  \advance\leftmarginii by 6pt
  \settowidth\leftmarginiii{\labelenumiii\hskip\labelsep}%
  \advance\leftmarginiii by 6pt
  \settowidth\leftmarginiv{\labelenumiv\hskip\labelsep}%
  \advance\leftmarginiv by 10pt
  \leftmarginv=10pt
  \leftmarginvi=10pt
  \leftmargin=\leftmargini
  \labelsep=5pt
  \labelwidth=\leftmargini \advance\labelwidth-\labelsep
  \@listi}
\newskip\listisep
\listisep\smallskipamount
\def\@listI{\leftmargin\leftmargini \parsep\z@skip
  \topsep\listisep \itemsep\z@skip
  \listparindent\normalparindent}
\let\@listi\@listI
\def\@listii{\leftmargin\leftmarginii
  \labelwidth\leftmarginii \advance\labelwidth-\labelsep
  \topsep\z@skip \parsep\z@skip \partopsep\z@skip \itemsep\z@skip}
\def\@listiii{\leftmargin\leftmarginiii
  \labelwidth\leftmarginiii \advance\labelwidth-\labelsep}
\def\@listiv{\leftmargin\leftmarginiv
  \labelwidth\leftmarginiv \advance\labelwidth-\labelsep}
\def\@listv{\leftmargin\leftmarginv
  \labelwidth\leftmarginv \advance\labelwidth-\labelsep}
\def\@listvi{\leftmargin\leftmarginvi
  \labelwidth\leftmarginvi \advance\labelwidth-\labelsep}

%%%% ooo begin
\def\@startsection#1#2#3#4#5#6{\if@noskipsec \leavevmode \fi
   \par \@tempskipa #4\relax
   \@afterindenttrue
   \ifdim \@tempskipa <\z@
     \@tempskipa -\@tempskipa \@afterindentfalse
   \fi
   \if@nobreak \everypar{}\else
     \addpenalty\@secpenalty\addvspace\@tempskipa
   \fi
   \@ifstar
     {\@ssect{#3}{#4}{#5}{#6}}%
     {\@dblarg{\@sect{#1}{#2}{#3}{#4}{#5}{#6}}}}
\def\@sect#1#2#3#4#5#6[#7]#8{%
     \ifnum #2>\c@secnumdepth
       \let\@svsec\@empty\else
       \refstepcounter{#1}%
       \protected@edef\@svsec{\@seccntformat{#1}\relax}%
     \fi
     \@tempskipa #5\relax
      \ifdim \@tempskipa>\z@
        \begingroup #6\relax
          \@hangfrom{\hskip #3\relax\@svsec}%
                    {\interlinepenalty \@M #8\par}%
        \endgroup
%       \csname #1mark\endcsname{#7}
       \csname #1mark\endcsname{\textsc{\csname the#1\endcsname. #7}}
         \addcontentsline{toc}{#1}{\ifnum #2>\c@secnumdepth \else
                      \protect\@numberline{\csname the#1\endcsname}\fi
                    #7}\else
        \def\@svsechd{#6\hskip #3\relax
                   \@svsec
             \@ifnotempty{#8}{\ignorespaces#8\unskip
             \@addpunct.}%
             \csname #1mark\endcsname
                      {#7}\addcontentsline
                           {toc}{#1}{\ifnum #2>\c@secnumdepth \else
                           \protect\@numberline{\csname the#1\endcsname}%
                                     \fi
                       #7}}\fi
     \@xsect{#5}}
\def\@xsect#1{\@tempskipa #1\relax
      \ifdim \@tempskipa>\z@
       \par \nobreak
       \vskip \@tempskipa
       \@afterheading
    \else \global\@nobreakfalse \global\@noskipsectrue
       \everypar{\if@noskipsec \global\@noskipsecfalse
                   \clubpenalty\@M \hskip -\parindent
                   \begingroup \@svsechd \endgroup \unskip
                   \@tempskipa #1\relax
                   \hskip -\@tempskipa
                  \else \clubpenalty \@clubpenalty
                    \everypar{}\fi}\fi\ignorespaces}
\def\@seccntformat#1{\csname the#1\endcsname.\quad}
\def\@ssect#1#2#3#4#5{\@tempskipa #3\relax
   \ifdim \@tempskipa>\z@
     \begingroup #4\@hangfrom{\hskip #1}{\interlinepenalty \@M #5\par}%
     \endgroup
   \else \def\@svsechd{#4\hskip #1\relax #5}\fi
    \@xsect{#3}}

%%%% ooo end

\newcounter{part}
\newcounter{chapter}
\newcounter{section}
\newcounter{subsection}[section]
\newcounter{subsubsection}[subsection]
\newcounter{paragraph}[subsubsection]
\renewcommand\thepart          {\arabic{part}}
\renewcommand\thechapter       {\arabic{chapter}}
\renewcommand\thesection       {\arabic{section}}
\renewcommand\thesubsection    {\thesection.\arabic{subsection}}
\renewcommand\thesubsubsection {\thesubsection .\arabic{subsubsection}}
\renewcommand\theparagraph     {\thesubsubsection.\arabic{paragraph}}
\setcounter{secnumdepth}{3}

\def\partname{Part}

\newif\if@part@
\@part@false

\newcommand\part{\par
\@part@true
   \addvspace{4ex}%
   \@afterindentfalse
   \secdef\@part\@spart}
\def\@part[#1]#2{%
    \ifnum \c@secnumdepth >\m@ne
      \refstepcounter{part}%
      \partmark{\textsc{\partname\ \thepart. #1}} %%% dddd
      \addcontentsline{toc}{part}{\partname~\thepart\unskip.\hspace{1em}#1}%
    \else
      \addcontentsline{toc}{part}{#1}%
    \fi
    {\parindent \z@ \centering
     \def\baselinestretch{1.2}
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >\m@ne
       \large\scshape \partname~\thepart
       \par\vskip 10pt \nobreak
     \fi
     \def\qwert{#2}
      \bfseries \uppercasenonmath\qwert\qwert
     \par}%
    \nobreak
    \vskip 3ex
    \@afterheading}
\def\@spart#1{%
    {\parindent \z@ \centering
     \interlinepenalty \@M
     \normalfont
     \def\qwert{#1}
      \bfseries \uppercasenonmath\qwert\qwert
      \par}%
     \nobreak
     \vskip 3ex
     \@afterheading}

%%%%%%%% chapter

\newif\if@chapter@
\@chapter@false

\newcommand\chapter{\par
\@chapter@true
   \addvspace{4ex}%
   \@afterindentfalse
   \secdef\@chapter\@schapter}
\def\@chapter[#1]#2{%
    \ifnum \c@secnumdepth >\m@ne
      \refstepcounter{chapter}%
      \chaptermark{\textsc{\chaptername\ \thechapter. #1}} %%% dddd
      \addcontentsline{toc}{chapter}{\chaptername~\thechapter\unskip.\hspace{1em}#1}%
    \else
      \addcontentsline{toc}{chapter}{#1}%
    \fi
    {\parindent \z@ \centering
     \def\baselinestretch{1.2}
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >\m@ne
       \large\scshape \chaptername~\thechapter
       \par\vskip 10pt \nobreak
     \fi
     \def\qwert{#2}
      \bfseries \uppercasenonmath\qwert\qwert
     \par}%
    \nobreak
    \vskip 3ex
    \@afterheading}
\def\@schapter#1{%
    {\parindent \z@ \centering
     \interlinepenalty \@M
     \normalfont
     \def\qwert{#1}
      \bfseries \uppercasenonmath\qwert\qwert
      \par}%
     \nobreak
     \vskip 3ex
     \@afterheading}



%%%%%%%%


\def\specialsection{\@startsection{section}{1}%
  \z@{\linespacing\@plus\linespacing}{.5\linespacing}%
  {\normalfont\centering}}
\def\section{\@startsection{section}{1}%
  \z@{.7\linespacing\@plus\linespacing}{.5\linespacing}%
  {\normalfont\scshape\centering}}
\def\subsection{\@startsection{subsection}{2}%
  \z@{.5\linespacing\@plus.7\linespacing}{-.5em}%
  {\normalfont\bfseries}}
\def\subsubsection{\@startsection{subsubsection}{3}%
  \z@{.5\linespacing\@plus.7\linespacing}{-.5em}%
  {\normalfont\itshape}}
\def\paragraph{\@startsection{paragraph}{4}%
  \z@\z@{-\fontdimen2\font}%
  \normalfont}
\def\subparagraph{\@startsection{subparagraph}{5}%
  \z@\z@{-\fontdimen2\font}%
  \normalfont}
\def\appendix{\par\c@section\z@ \c@subsection\z@
   \let\sectionname\appendixname
   \def\thesection{\@Alph\c@section}}
\def\appendixname{Appendix}
\def\@Roman#1{\@xp\@slowromancap
  \romannumeral#1@}%
\def\@slowromancap#1{\ifx @#1% then terminate
  \else
    \if i#1I\else\if v#1V\else\if x#1X\else\if l#1L\else\if
    c#1C\else\if m#1M\else#1\fi\fi\fi\fi\fi\fi
    \@xp\@slowromancap
  \fi
}
\def\@starttoc#1#2{\begingroup
  \par\removelastskip\vskip\z@skip
  \@startsection{}\@M\z@{\linespacing\@plus\linespacing}%
    {.5\linespacing}{\centering\scshape}{#2}%
  \ifx\contentsname#2%
  \else \addcontentsline{toc}{section}{#2}\fi
  \makeatletter
  \@input{\jobname.#1}%
  \if@filesw
    \@xp\newwrite\csname tf@#1\endcsname
    \immediate\@xp\openout\csname tf@#1\endcsname \jobname.#1\relax
  \fi
  \global\@nobreakfalse \endgroup
  \addvspace{32\p@\@plus14\p@}%
  \let\tableofcontents\relax
}
\def\contentsname{Contents}
\def\listfigurename{List of Figures}
\def\listtablename{List of Tables}
\def\listoffigures{\@starttoc{lof}\listfigurename}
\def\listoftables{\@starttoc{lot}\listtablename}
\AtBeginDocument{%
  \@for\@tempa:=-1,0,1,2,3\do{%
    \@ifundefined{r@tocindent\@tempa}{%
      \@xp\gdef\csname r@tocindent\@tempa\endcsname{0pt}}{}%
  }%
}
\def\@writetocindents{%
  \begingroup
  \@for\@tempa:=-1,0,1,2,3\do{%
    \immediate\write\@auxout{%
      \string\newlabel{tocindent\@tempa}{%
        \csname r@tocindent\@tempa\endcsname}}%
  }%
  \endgroup}
\AtEndDocument{\@writetocindents\label{ENDPAGE}}

\let\indentlabel\@empty
\def\@tochangmeasure#1{\sbox\z@{#1}%
  \ifdim\wd\z@>\csname r@tocindent\@toclevel\endcsname\relax
    \@xp\xdef\csname r@tocindent\@toclevel\endcsname{\the\wd\z@}%
  \fi
}

%%%% ooo begin
\newcommand\@pnumwidth{1.55em}
\newcommand\@tocrmarg{2.55em}
\newcommand\@dotsep{4.5}
\setcounter{tocdepth}{3}

\def\Contentsname{Ñîäåðæàíèå}
\newcommand\tableofcontents{
    \section*{\bf\uppercasenonmath\Contentsname\small\Contentsname}
    \makeatletter
  \begingroup
  \@input{\jobname.toc}%
  \if@filesw
    \@xp\newwrite\csname tf@toc\endcsname
    \immediate\@xp\openout\csname tf@toc\endcsname \jobname.toc\relax
  \fi
  \global\@nobreakfalse \endgroup
  \makeatother
  \addvspace{32\p@\@plus14\p@}%
  \let\tableofcontents\relax
    }

\def\@numberline#1{\hb@xt@\@tempdima{\hfil#1\unskip.\ }}

\newcommand*\l@part{\@dottedtocline{1}{0pt}{5 em}}
\newcommand*\l@chapter{\@dottedtocline{1}{0pt}{5 em}}

\newcommand*\l@section{\@dottedtocline{1}{0em}{2.3em}}
\newcommand*\l@subsection{\@dottedtocline{2}{2em}{3.3em}}

\newcommand*\l@subsubsection{\@dottedtocline{3}{3.8em}{3.2em}}
\newcommand*\l@paragraph{\@dottedtocline{4}{7.0em}{4.1em}}
\newcommand*\l@subparagraph{\@dottedtocline{5}{10em}{5em}}

%%%% ooo end

\let\tocappendix\tocchapter
\def\l@figure{\@tocline{0}{3pt plus2pt}{0pt}{}{}}
\let\l@table=\l@figure
\def\refname{References}
\def\bibname{Bibliography}
\def\bibliographystyle#1{%
   \if@filesw\immediate\write\@auxout
    {\string\bibstyle{#1}}\fi
        \def\@tempa{#1}%
        \def\@tempb{amsplain}%
        \def\@tempc{}%
        \ifx\@tempa\@tempb
                \def\@biblabel##1{##1.}%
                \def\bibsetup{}%
        \else
                \def\bibsetup{\labelsep6\p@}%
        \ifx\@tempa\@tempc
                \def\@biblabel##1{}%
                \def\bibsetup{\labelwidth\z@ \leftmargin24\p@
                \itemindent-24\p@
                          \labelsep\z@ }%
        \fi
\fi}

\def\Refname{Ñïèñîê ëèòåðàòóðû}
\newenvironment{thebibliography}[1]{%
   \section*{\bf\uppercasenonmath\Refname\small\Refname}
       \partmark{\textsc{\Refname}}
       \chaptermark{\textsc{\Refname}}
       \sectionmark{\textsc{\Refname}}
  \if@chapter@
      \addcontentsline{toc}{chapter}{\refname}
      \else
      \addcontentsline{toc}{section}{\hspace*{2.3em}\refname}
  \fi
   \small
  \renewcommand\theenumiv{\arabic{enumiv}}\let\p@enumiv\@empty
  \list{\theenumiv\unskip.}{\settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth \advance\leftmargin\labelsep
    \usecounter{enumiv}}%
  \sloppy \clubpenalty\@M \widowpenalty\clubpenalty
  \sfcode`\.=\@m
}{%
  \def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
  \endlist
}


\def\bysame{\leavevmode\hbox to3em{\hrulefill}\thinspace}
\def\newblock{}
\newif\if@restonecol
\def\theindex{\@restonecoltrue\if@twocolumn\@restonecolfalse\fi
  \columnseprule\z@ \columnsep 35\p@
  \twocolumn[\@xp\section\@xp*\@xp{\indexname}]%
  \thispagestyle{plain}%
  \let\item\@idxitem
  \parindent\z@  \parskip\z@\@plus.3\p@\relax
  \footnotesize}
\def\indexname{Index}
\def\@idxitem{\par\hangindent 2em}
\def\subitem{\par\hangindent 2em\hspace*{1em}}
\def\subsubitem{\par\hangindent 3em\hspace*{2em}}
\def\endtheindex{\if@restonecol\onecolumn\else\clearpage\fi}
\def\indexspace{\par\bigskip}
\def\footnoterule{\kern-.4\p@
        \hrule\@width 5pc\kern11\p@\kern-\footnotesep}
\def\@makefnmark{\hbox{$\m@th^{\@thefnmark}$}}
\def\@makefntext{\indent\@makefnmark}
\long\def\@footnotetext#1{\insert\footins{%
  \normalfont\footnotesize
  \interlinepenalty\interfootnotelinepenalty
  \splittopskip\footnotesep \splitmaxdepth \dp\strutbox
  \floatingpenalty\@MM \hsize\columnwidth
  \@parboxrestore \parindent\normalparindent \sloppy
  \edef\@currentlabel{\p@footnote\@thefnmark}%
  \@makefntext{\rule\z@\footnotesep\ignorespaces#1\unskip\strut\par}}}
\hfuzz=1pt \vfuzz=\hfuzz
\def\sloppy{\tolerance9999 \emergencystretch 3em\relax}
\setcounter{topnumber}{4}
\setcounter{bottomnumber}{4}
\setcounter{totalnumber}{4}
\setcounter{dbltopnumber}{4}
\renewcommand{\topfraction}{.97}
\renewcommand{\bottomfraction}{.97}
\renewcommand{\textfraction}{.03}
\renewcommand{\floatpagefraction}{.9}
\renewcommand{\dbltopfraction}{.97}
\renewcommand{\dblfloatpagefraction}{.9}
\setlength{\floatsep}{12pt plus 6pt minus 4pt}
\setlength{\textfloatsep}{15pt plus 8pt minus 5pt}
\setlength{\intextsep}{12pt plus 6pt minus 4pt}
\setlength{\dblfloatsep}{12pt plus 6pt minus 4pt}
\setlength{\dbltextfloatsep}{15pt plus 8pt minus 5pt}
\setlength{\@fptop}{0pt}% removed ``plus 1fil''
\setlength{\@fpsep}{8pt}% removed ``plus 2fil''
\setlength{\@fpbot}{0pt plus 1fil}
\setlength{\@dblfptop}{0pt}% removed ``plus 1fil''
\setlength{\@dblfpsep}{8pt}% removed ``plus 2fil''
\setlength{\@dblfpbot}{0pt plus 1fil}
\newcommand{\fps@figure}{tbp}
\newcommand{\fps@table}{tbp}
\newcounter{figure}
\def\captionheadfont@{\scshape}
\def\captionfont@{\normalfont}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurename\ \thefigure}
\def\figurename{Figure}
\def\figure{\@float{figure}}
\let\endfigure=\end@float
\newcounter{table}
\def\ftype@table{2}
\def\ext@table{lot}
\def\fnum@table{\tablename\ \thetable}
\def\tablename{Table}
\def\table{\@float{table}}
\let\endtable=\end@float
\long\def\@makecaption#1#2{%
  \setbox\@tempboxa\vbox{\color@setgroup
    \advance\hsize-6pc\noindent
    \captionfont@\captionheadfont@#1\@xp\@ifnotempty\@xp
        {\@cdr#2\@nil}{.\captionfont@\upshape\enspace#2}%
    \unskip\kern-6pc\par
    \global\setbox\@ne\lastbox\color@endgroup}%
  \ifhbox\@ne % the normal case
    \setbox\@ne\hbox{\unhbox\@ne\unskip\unskip\unpenalty\unkern}%
  \fi
  \ifdim\wd\@tempboxa=\z@ % this means caption will fit on one line
    \setbox\@ne\hbox to\columnwidth{\hss\kern-6pc\box\@ne\hss}%
  \else % tempboxa contained more than one line
    \setbox\@ne\vbox{\unvbox\@tempboxa\parskip\z@skip
        \noindent\unhbox\@ne\advance\hsize-6pc\par}%
\fi
  \ifnum\@tempcnta<64 % if the float IS a figure...
    \addvspace\abovecaptionskip
    \moveright 3pc\box\@ne
  \else % if the float IS NOT a figure...
    \moveright 3pc\box\@ne
    \nobreak
    \vskip\belowcaptionskip
  \fi
\relax
}
\newskip\abovecaptionskip \abovecaptionskip=12pt \relax
\newskip\belowcaptionskip \belowcaptionskip=12pt \relax
\@ifpackageloaded{amsgen}{}{\input{amsgen.sty}}
\newcommand{\theoremstyle}[1]{%
  \@ifundefined{th@#1}{%
    \PackageWarning{amsthm}{Unknown theoremstyle `#1'}%
    \theorem@style{plain}%
  }{%
    \theorem@style{#1}%
  }%
}
\newtoks\theorem@style
\theorem@style{plain}
\newtoks\theorembodyfont
\theorembodyfont{\itshape}
\newtoks\theoremheadfont
\theoremheadfont{\bfseries}
\newtoks\theoremnotefont
\theoremnotefont{\bfseries}
\newtoks\theoremheadpunct
\theoremheadpunct{.}
\newskip\theorempreskipamount \theorempreskipamount\topsep
\newskip\theorempostskipamount \theorempostskipamount\topsep
\renewcommand{\newtheorem}{\@ifstar{\@xnthm *}{\@xnthm \relax}}
\def\@xnthm#1#2{%
  \let\@tempa\relax
  \@xp\@ifdefinable\csname #2\endcsname{%
    \global\@xp\let\csname end#2\endcsname\@endtheorem
    \ifx *#1% unnumbered, need to get one more mandatory arg
      \edef\@tempa##1{%
        \gdef\@xp\@nx\csname#2\endcsname{%
          \@nx\@thm{\@xp\@nx\csname th@\the\theorem@style\endcsname}%
            {}{##1}}}%
    \else % numbered theorem, need to check for optional arg
      \def\@tempa{\@oparg{\@ynthm{#2}}[]}%
    \fi
  }%
  \@tempa
}
\def\@ynthm#1[#2]#3{%
  \ifx\relax#2\relax
    \def\@tempa{\@oparg{\@xthm{#1}{#3}}[]}%
  \else
    \@ifundefined{c@#2}{%
      \def\@tempa{\@nocounterr{#2}}%
    }{%
      \@xp\xdef\csname the#1\endcsname{\@xp\@nx\csname the#2\endcsname}%
      \toks@{#3}%
      \@xp\xdef\csname#1\endcsname{%
        \@nx\@thm{%
          \let\@nx\thm@swap
            \if S\thm@swap\@nx\@firstoftwo\else\@nx\@gobble\fi
          \@xp\@nx\csname th@\the\theorem@style\endcsname}%
            {#2}{\the\toks@}}%
      \let\@tempa\relax
    }%
  \fi
  \@tempa
}
\def\@xthm#1#2[#3]{%
  \ifx\relax#3\relax
    \newcounter{#1}%
  \else
    \newcounter{#1}[#3]%
    \@xp\xdef\csname the#1\endcsname{\@xp\@nx\csname the#3\endcsname
      \@thmcountersep\@thmcounter{#1}}%
  \fi
  \toks@{#2}%
  \@xp\xdef\csname#1\endcsname{%
    \@nx\@thm{%
      \let\@nx\thm@swap
        \if S\thm@swap\@nx\@firstoftwo\else\@nx\@gobble\fi
      \@xp\@nx\csname th@\the\theorem@style\endcsname}%
      {#1}{\the\toks@}}%
}
\def\@thm#1#2#3{\normalfont
  \trivlist
  \labelsep.5em\relax \let\thmheadnl\relax
  \let\theoremindent\noindent % no indent
  \let\thm@swap\@gobble
  \theoremheadfont{\bfseries}% heading font bold
  \theoremheadpunct{.}% add period after heading
  \theorempreskipamount\topsep
  \theorempostskipamount\theorempreskipamount
  #1% style overrides
  \@topsep \theorempreskipamount               % used by first \item
  \@topsepadd \theorempostskipamount           % used by \@endparenv
  \def\@tempa{#2}\ifx\@empty\@tempa
    \def\@tempa{\@oparg{\@begintheorem{#3}{}}[]}%
  \else
    \refstepcounter{#2}%
    \def\@tempa{\@oparg{\@begintheorem{#3}{\csname the#2\endcsname}}[]}%
  \fi
  \@tempa
}
\let\@ythm\relax
\let\thmname\@iden \let\thmnumber\@iden \let\thmnote\@iden
\def\thmhead@plain#1#2#3{%
  \thmname{#1}\thmnumber{ #2}\thmnote{ {\the\theoremnotefont(#3)}}}
\let\thmhead\thmhead@plain
\def\swappedhead#1#2#3{%
  \thmnumber{#2}\thmname{. #1}\thmnote{ {\the\theoremnotefont(#3)}}}
\let\thmheadnl\relax
\def\@begintheorem#1#2[#3]{%
  \item[\normalfont % reset in case body font is abnormal
  \hskip\labelsep
  \the\theoremheadfont
  \theoremindent
  \@ifempty{#1}{\let\thmname\@gobble}{\let\thmname\@iden}%
  \@ifempty{#2}{\let\thmnumber\@gobble}{\let\thmnumber\@iden}%
  \@ifempty{#3}{\let\thmnote\@gobble}{\let\thmnote\@iden}%
  \thm@swap\swappedhead\thmhead{#1}{#2}{#3}%
  \the\theoremheadpunct]%
  \thmheadnl % possibly a newline.
  \ignorespaces}
\def\nonslanted{\relax
  \@xp\let\@xp\@tempa\csname\f@shape shape\endcsname
  \ifx\@tempa\itshape\upshape
  \else\ifx\@tempa\slshape\upshape\fi\fi}
\def\swapnumbers{\edef\thm@swap{\if S\thm@swap N\else S\fi}}
\def\thm@swap{N}%
\let\@opargbegintheorem\relax
\def\th@plain{%
%%  \let\theoremindent\noindent % no indent
%%  \theoremheadfont{\bfseries}% heading font is bold
%%  \theoremnotefont{}% same as heading font
%%  \theoremheadpunct{.}% add period after heading
%%  \let\thm@swap\@gobble
%%  \theorempreskipamount\topsep
%%  \theorempostskipamount\theorempreskipamount
  \itshape % body font
}
\def\th@definition{%
  \normalfont % body font
}
\def\th@remark{%
  \theoremheadfont{\itshape}%
  \normalfont % body font
  \theorempreskipamount\topsep
  \divide\theorempreskipamount\tw@
  \theorempostskipamount\theorempreskipamount
}
\def\@endtheorem{\endtrivlist\@endpefalse }
\newcommand{\newtheoremstyle}[9]{%
  \@ifempty{#5}{\dimen@\z@skip}{\dimen@#5\relax}%
  \ifdim\dimen@=\z@
    \toks@{#4\let\theoremindent\noindent}%
  \else
    \toks@{#4\def\theoremindent{\noindent\hbox to#5{}}}%
  \fi
  \def\@tempa{#8}\ifx\space\@tempa
    \toks@\@xp{\the\toks@ \labelsep\fontdimen\tw@\font\relax}%
  \else
    \def\@tempb{\newline}%
    \ifx\@tempb\@tempa
      \toks@\@xp{\the\toks@ \labelsep\z@skip
        \def\thmheadnl{\leavevmode\newline}}%
    \else
      \toks@\@xp{\the\toks@ \labelsep#8\relax}%
    \fi
  \fi
  \@temptokena{%
    \theorempreskipamount#2\relax
    \theorempostskipamount#3\relax
    \theoremheadfont{#6}\theoremheadpunct{#7}%
  }%
  \@ifempty{#9}{%
    \let\thmhead\thmhead@plain
  }{%
    \@namedef{thmhead@#1}##1##2##3{#9}%
    \@temptokena\@xp{\the\@temptokena
      \@xp\let\@xp\thmhead\csname thmhead@#1\endcsname}%
  }%
  \@xp\xdef\csname th@#1\endcsname{\the\toks@ \the\@temptokena}%
}
\DeclareRobustCommand{\qed}{%
  \ifmmode % if math mode, assume display: omit penalty etc.
  \else \leavevmode\unskip\penalty9999 \hbox{}\nobreak\hfill
  \fi
  \quad\hbox{\qedsymbol}}
\newcommand{\openbox}{\leavevmode
  \hbox to.77778em{%
  \hfil\vrule
  \vbox to.675em{\hrule width.6em\vfil\hrule}%
  \vrule\hfil}}
\newcommand{\qedsymbol}{\openbox}
\newenvironment{proof}[1][\proofname.]{\par
  \normalfont
  \topsep6\p@\@plus6\p@ \trivlist
  \item[\hskip\labelsep\itshape
%    #1\@addpunct{.}]\ignorespaces
    #1]\ignorespaces
}{%
  \qed\endtrivlist
}
\newcommand{\proofname}{Proof}

%\DeclareOption*{\input{\CurrentOption .thm}}
%\ProcessOptions

%%%%% amsthm

\def\@swapped#1#2{#2%
  \@ifnotempty{#1}{\@addpunct{.}\quad#1\unskip}}
\def\th@plain{%
  \let\theoremindent\indent
  \theoremnotefont{\mdseries\upshape}%
  \theorempreskipamount.5\baselineskip\@plus.2\baselineskip
                                    \@minus.2\baselineskip
  \theorempostskipamount\theorempreskipamount
  \itshape
}
\def\th@definition{%
  \let\theoremindent\indent
  \theoremnotefont{\mdseries\upshape}%
  \theorempreskipamount.5\baselineskip\@plus.2\baselineskip
                                    \@minus.2\baselineskip
  \theorempostskipamount\theorempreskipamount
  \upshape
}
\def\th@remark{%
  \let\theoremindent\indent
  \theoremheadfont{\itshape}% heading font bold
  \theoremnotefont{\mdseries\upshape}%
  \theorempreskipamount.5\baselineskip\@plus.2\baselineskip
                                    \@minus.2\baselineskip
  \theorempostskipamount\theorempreskipamount
  \upshape
}
\if@compatibility
\let\@newpf\proof \let\proof\relax \let\endproof\relax
\newenvironment{pf}{\@newpf[\proofname]}{\qed\endtrivlist}
\newenvironment{pf*}[1]{\@newpf[#1]}{\qed\endtrivlist}
\fi
\def\nonbreakingspace{\unskip\nobreak\ \ignorespaces}
\def~{\protect\nonbreakingspace}
\def\@biblabel#1{\@ifnotempty{#1}{[#1]}}
\def\@cite#1#2{{%
  \m@th\upshape\mdseries[{#1\if@tempswa, #2\fi}]}}
\@ifundefined{cite }{%
  \expandafter\let\csname cite \endcsname\cite
  \edef\cite{\@nx\protect\@xp\@nx\csname cite \endcsname}%
}{}
\def\fullwidthdisplay{\displayindent\z@ \displaywidth\columnwidth}
\edef\@tempa{\noexpand\fullwidthdisplay\the\everydisplay}
\everydisplay\expandafter{\@tempa}
\newcommand\seename{see also}%
\newcommand\see[2]{{\em \seename\/} #1}%
\newcommand\printindex{\@input{\jobname.ind}}%
\hyphenation{acad-e-my acad-e-mies af-ter-thought anom-aly anom-alies
an-ti-deriv-a-tive an-tin-o-my an-tin-o-mies apoth-e-o-ses
apoth-e-o-sis ap-pen-dix ar-che-typ-al as-sign-a-ble as-sist-ant-ship
as-ymp-tot-ic asyn-chro-nous at-trib-uted at-trib-ut-able bank-rupt
bank-rupt-cy bi-dif-fer-en-tial blue-print busier busiest
cat-a-stroph-ic cat-a-stroph-i-cally con-gress cross-hatched data-base
de-fin-i-tive de-riv-a-tive dis-trib-ute dri-ver dri-vers eco-nom-ics
econ-o-mist elit-ist equi-vari-ant ex-quis-ite ex-tra-or-di-nary
flow-chart for-mi-da-ble forth-right friv-o-lous ge-o-des-ic
ge-o-det-ic geo-met-ric griev-ance griev-ous griev-ous-ly
hexa-dec-i-mal ho-lo-no-my ho-mo-thetic ideals idio-syn-crasy
in-fin-ite-ly in-fin-i-tes-i-mal ir-rev-o-ca-ble key-stroke
lam-en-ta-ble light-weight mal-a-prop-ism man-u-script mar-gin-al
meta-bol-ic me-tab-o-lism meta-lan-guage me-trop-o-lis
met-ro-pol-i-tan mi-nut-est mol-e-cule mono-chrome mono-pole
mo-nop-oly mono-spline mo-not-o-nous mul-ti-fac-eted mul-ti-plic-able
non-euclid-ean non-iso-mor-phic non-smooth par-a-digm par-a-bol-ic
pa-rab-o-loid pa-ram-e-trize para-mount pen-ta-gon phe-nom-e-non
post-script pre-am-ble pro-ce-dur-al pro-hib-i-tive pro-hib-i-tive-ly
pseu-do-dif-fer-en-tial pseu-do-fi-nite pseu-do-nym qua-drat-ic
quad-ra-ture qua-si-smooth qua-si-sta-tion-ary qua-si-tri-an-gu-lar
quin-tes-sence quin-tes-sen-tial re-arrange-ment rec-tan-gle
ret-ri-bu-tion retro-fit retro-fit-ted right-eous right-eous-ness
ro-bot ro-bot-ics sched-ul-ing se-mes-ter semi-def-i-nite
semi-ho-mo-thet-ic set-up se-vere-ly side-step sov-er-eign spe-cious
spher-oid spher-oid-al star-tling star-tling-ly sta-tis-tics
sto-chas-tic straight-est strange-ness strat-a-gem strong-hold
sum-ma-ble symp-to-matic syn-chro-nous topo-graph-i-cal tra-vers-a-ble
tra-ver-sal tra-ver-sals treach-ery turn-around un-at-tached
un-err-ing-ly white-space wide-spread wing-spread wretch-ed
wretch-ed-ly Eng-lish Euler-ian Feb-ru-ary Gauss-ian
Hamil-ton-ian Her-mit-ian Jan-u-ary Japan-ese Kor-te-weg
Le-gendre Mar-kov-ian Noe-ther-ian No-vem-ber Rie-mann-ian Sep-tem-ber}
\def\calclayout{\advance\textheight -\headheight
  \advance\textheight -\headsep
  \oddsidemargin\paperwidth
  \advance\oddsidemargin -\textwidth
  \divide\oddsidemargin\tw@
  \ifdim\oddsidemargin<.5truein \oddsidemargin.5truein \fi
  \advance\oddsidemargin -1truein
  \evensidemargin\oddsidemargin
  \topmargin\paperheight \advance\topmargin -\textheight
  \advance\topmargin -\headheight \advance\topmargin -\headsep
  \divide\topmargin\tw@
  \ifdim\topmargin<.5truein \topmargin.5truein \fi
%  \advance\topmargin -\footskip
  \advance\topmargin -1truein\relax
}
\calclayout % initialize
\pagenumbering{arabic}
\pagestyle{headings}
\thispagestyle{plain}
%\if@compatibility \else\endinput\fi
\def\tiny{\Tiny}
\def\defaultfont{\normalfont}
\def\rom{\textup}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifx \fnpp@loaded\undefined
    \def\fnpp@loaded{$StyleRevision: 2.6 $}
\else
    \PackageWarningNoLine{footnpag}%
        {Some other package already uses namespace `fnpp'}
\fi

\begingroup
    \def\RCSPackage#1#2 $#3: #4 #5\endRCS $#6: #7 #8\endRCS{%
    \def\date{#4}\def\id{v#7}%
    \ProvidesPackage{#1}[\date\space\id\space #2]%
    }

  \RCSPackage{footnpag}{numbering footnotes per page}
  $StyleDate: 1995/11/10 18:21:26 $: 9999/00/00 \endRCS
  $StyleRevision: 2.6 $: 0.0 \endRCS
\endgroup

\ifx \CatEscape\undefined
    \chardef\CatEscape=0
    \chardef\CatOpen=1
    \chardef\CatClose=2
    \chardef\CatIgnore=9
    \chardef\CatLetter=11
    \chardef\CatOther=12
    \chardef\CatActive=13       % is defined in Plain already

    \chardef\CatUsCode=\catcode`\_
\fi

\catcode`\_=\CatLetter          % top level macro file
\newread\old_foot_file
\newwrite\foot_file
\def\foot_file_name{\jobname.fot\relax}
\def\init_footnote{%
   \openin\old_foot_file\foot_file_name
   \ifeof\old_foot_file  \closein\old_foot_file
   \else  \closein\old_foot_file
      \read_foot_file
   \fi
   \immediate\openout\foot_file\foot_file_name
   \immediate\write\foot_file{\relax}%
   \global\let\init_footnote\relax
   }
\newcount\foot_name_no  % for generating footnote mark names

\def\fnpp_next_footnote{%
    \init_footnote
    \global\advance\foot_name_no\@ne
    \edef\do_write{%
    \write\foot_file{%
        \string\advance\c@footnote\@ne
        \string\expandafter\xdef
            \string\csname\space f@\number\foot_name_no \endcsname{%
        \string\number\c@footnote
        }%
        }%
    }%
    \do_write
    \global\c@footnote 0\csname f@\number\foot_name_no \endcsname \relax
    }


\def\read_foot_file{%
   \begingroup
      \catcode`\@\CatLetter \catcode`\^^M\CatIgnore
      \input \foot_file_name
   \endgroup
   }

\let\fnpp_orig_outputpage=\@outputpage
\def\@outputpage{%
    \ifx \init_footnote\relax
    \immediate\write\foot_file{\c@footnote\z@}%
    \fi
    \fnpp_orig_outputpage
    }

\let\FnppOrigFootnote=\footnote     % save original bindings
\let\FnppOrigFootnotemark=\footnotemark

\def\footnote{%
    \@ifnextchar[%          % ] (Emacs)
    \@xfootnote
    {\fnpp_next_footnote \@xfootnote[\the\c@footnote]}%
    }
\def\footnotemark{%
    \@ifnextchar[%          % ] (Emacs)
    \@xfootnotemark
    {\fnpp_next_footnote \@xfootnotemark[\the\c@footnote]}%
    }
\ifx \@minipagerestore\relax
    \let\@minipagerestore\@empty
\fi

\g@addto@macro\@minipagerestore{%
    \let\footnote\FnppOrigFootnote
    }
\let\fnpp_orig_maketitle=\maketitle
\def\maketitle{%
    \begingroup
        \let\footnotemark\FnppOrigFootnotemark
    \fnpp_orig_maketitle
    \endgroup
    }

\catcode`\_=\CatUsCode


\input amssymb.sty
\def\leq{\leqslant} \let\le\leq
\def\geq{\geqslant} \let\ge\geq

\tolerance=5000
\hfuzz=2pt
\vfuzz=2pt

\def\CONTNAME{Ñîäåðæàíèå}

\newcommand\tocline[4][]{%
\smallskip
\@dottedtocline{1}{0pt}{1em}{#2
 \ifthenelse{\equal{#1}{*}}{}{\protect\\}
 ({\it #3}\/)}{#4}}
\uppercasenonmath\CONTNAME

\newenvironment{globalcontents}{
\thispagestyle{empty}
\pagestyle{empty}
\vspace*{2cm}
\normalfont
\begin{center}
\bfseries\CONTNAME
\end{center}
\vspace*{1cm}}{\relax}

\renewcommand{\descriptionlabel}[1]{\textbf{#1}}
\renewcommand{\labelenumi}{\theenumi)}


\let\@subtitle\@empty
\def\subtitle#1{\def\@subtitle{#1}}
\long\def\maketitlepage{%
\thispagestyle{empty}\pagestyle{empty}
%
\vspace{2cm}
\begin{center}
 \Large \bfseries
 ÐÅÄÀÊÖÈÎÍÍÀß ÊÎËËÅÃÈß
\end{center}
\vspace{0.5cm}
\begin{flushleft}
 \Large
\textbf{Ãëàâíûé ðåäàêòîð:}
\\[5pt]
\textit{Ð.~Â.~Ãàìêðåëèäçå} (Ìàòåìàòè÷åñêèé èíñòèòóò èì. Â.~À.~Ñòåêëîâà ÐÀÍ)
%
\\[10pt]
%
\textbf{Çàìåñòèòåëè ãëàâíîãî ðåäàêòîðà:}
\\[5pt]
\textit{À.~Â.~Îâ÷èííèêîâ} (ÌÃÓ èì. Ì.~Â.~Ëîìîíîñîâà)
\\
\textit{Â.~Ë.~Ïîïîâ} (Ìàòåìàòè÷åñêèé èíñòèòóò èì. Â.~À.~Ñòåêëîâà ÐÀÍ)
\\[10pt]
%
\textbf{×ëåíû ðåäêîëëåãèè:}
\\[5pt]
\textit{À.~À.~Àãðà÷\"åâ} (Ìàòåìàòè÷åñêèé èíñòèòóò èì. Â.~À.~Ñòåêëîâà ÐÀÍ, SISSA)
\\
\textit{Å.~Ñ.~Ãîëîä} (ÌÃÓ èì. Ì.~Â.~Ëîìîíîñîâà)
\\
\textit{À.~Á.~Æèæ÷åíêî} (Îòäåëåíèå ìàòåìàòè÷åñêèõ íàóê ÐÀÍ)
\\
\textit{Å.~Ï.~Êðóãîâà} (ÂÈÍÈÒÈ ÐÀÍ)
\\
\textit{À.~Â.~Ìèõàë\"åâ} (ÌÃÓ èì. Ì.~Â.~Ëîìîíîñîâà)
\\
\textit{È.~Þ.~Íèêîëüñêàÿ} (ÂÈÍÈÒÈ ÐÀÍ)
\\
\textit{Í.~Õ.~Ðîçîâ} (ÌÃÓ èì. Ì.~Â.~Ëîìîíîñîâà)
\\
\textit{Ì.~Â.~Øàìîëèí} (Èíñòèòóò ìåõàíèêè ÌÃÓ èì. Ì.~Â.~Ëîìîíîñîâà)
%
\\[10pt]
%
\textbf{Îòâåòñòâåííûå ðåäàêòîðû:}
\\[5pt]
\textit{È. À. Æëÿáèíêîâà}
\\
\textit{Í. Þ. Ñåëèâàíîâà}
\\[10pt]
 \@RedSost
%
%\textbf{Àâòîð:}
%\\[5pt]
%\itshape\andify\authors\authors
\end{flushleft}
%
\let\enddoc@text\relax
\vfill
\eject

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\begin{flushright}
 \Large \bfseries  ISSN~\ISSN
\end{flushright}
%
\vspace{5mm}
%
\begin{center}
\Large\bfseries
 ÐÎÑÑÈÉÑÊÀß ÀÊÀÄÅÌÈß ÍÀÓÊ
 \\[10pt]
 ÂÑÅÐÎÑÑÈÉÑÊÈÉ ÈÍÑÒÈÒÓÒ
 \\
 ÍÀÓ×ÍÎÉ È ÒÅÕÍÈ×ÅÑÊÎÉ ÈÍÔÎÐÌÀÖÈÈ
 \\
 (ÂÈÍÈÒÈ ÐÀÍ)
\end{center}
%
\vspace{1cm}
%
\begin{center}
 \Huge
% \LARGE
 \bfseries
 ÈÒÎÃÈ ÍÀÓÊÈ È ÒÅÕÍÈÊÈ
 \\[15pt]
 \huge
 ÑÅÐÈß
 \\
 ÑÎÂÐÅÌÅÍÍÀß ÌÀÒÅÌÀÒÈÊÀ
 \\
 È ÅÅ ÏÐÈËÎÆÅÍÈß
 \\[15pt]
 ÒÅÌÀÒÈ×ÅÑÊÈÅ ÎÁÇÎÐÛ
\end{center}
%
\vspace{15mm}
%
\begin{center}
\Huge \bfseries Òîì \@currentvolume
\end{center}
%
\vspace{1cm}
%
\begin{center}
\LARGE \bfseries\uppercasenonmath\@title\@title
\end{center}
\vfill
\begin{center}
\Large \bfseries
 \includegraphics[width=25mm]{viniti.eps}\\[1cm]
 Ìîñêâà \ \@currentyear
\end{center}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\eject
%


}

\newcommand{\myandify}{%
  \nxandlist{\unskip, }{\unskip{}, }{\unskip, }}

%\newcommand{\myandify}{%
%  \nxandlist{\unskip, }{\unskip{}, }{\unskip, }}

\newcounter{ForQED}
\setcounter{ForQED}{0}
\renewenvironment{proof}[1][Äîêàçàòåëüñòâî. ]%
 {\smallskip\noindent{\itshape #1}\setcounter{ForQED}{0}}%
 {\ifthenelse{\value{ForQED}=0}{\hfill$\Box$}{}%
 \setcounter{ForQED}{0}%
 \par\smallskip}%
\gdef\qedhere{\setcounter{ForQED}{1}\tag*{$\Box$}}
\gdef\Qedhere{\setcounter{ForQED}{1}\hfill$\Box$}

\def\@RedSost{\relax}
\def\RedSost#1{\gdef\@RedSost{#1}}

%\def\No{\symbol{157}}
\def\No{\textnumero}
\def\firstpage#1{\setcounter{page}{#1}}


\endinput
%%
%% End of file `amsart.cls'.
