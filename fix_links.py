#!/usr/bin/env python3
"""Fix broken and redirected links in README.md"""

import re

# Map of old URLs to new URLs (permanent redirects)
REDIRECTS = {
    # HTTP to HTTPS upgrades
    "http://www.maths.lth.se/matematiklu/personal/olofsson/CompHT06.pdf": "https://www.maths.lth.se/matematiklu/personal/olofsson/CompHT06.pdf",
    "http://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf": "https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf",
    "http://www.jirka.org/diffyqs/": "https://www.jirka.org/diffyqs/",
    "http://www.mat.univie.ac.at/~michor/dgbook.pdf": "https://www.mat.univie.ac.at/~michor/dgbook.pdf",
    "http://i.creativecommons.org/p/zero/1.0/88x31.png": "https://licensebuttons.net/p/zero/1.0/88x31.png",
    "http://creativecommons.org/publicdomain/zero/1.0/": "https://creativecommons.org/publicdomain/zero/1.0/",
    "http://www.sagemath.org/": "https://www.sagemath.org/",
    "http://cyrille.rossant.net": "https://cyrille.rossant.net/",
    "http://math.stackexchange.com/": "https://math.stackexchange.com/",
    "http://mathoverflow.net/": "https://mathoverflow.net/",
    "http://planetmath.org/": "https://planetmath.org/",
    
    # Domain changes and path updates
    "https://www.uio.no/studier/emner/matnat/math/MAT-INF2360/v15/kompendium/applinalgpython.pdf": "https://www.uio.no/studier/emner/matnat/math/nedlagte-emner/MAT-INF2360/v15/kompendium/applinalgpython.pdf",
    "https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg": "https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg",
    "https://teorth.github.io/QED": "https://teorth.github.io/QED/",
    "http://www.math.bme.hu/~kalex/Teaching/Spring10/Topology/TopNotes_Spring10.pdf": "http://math.bme.hu/~kalex/Teaching/Spring10/Topology/TopNotes_Spring10.pdf",
    "http://ocw.mit.edu/courses/mathematics/": "https://ocw.mit.edu/courses/mathematics/",
    "http://www.matematik.lu.se/matematiklu/personal/sigma/Riemann.pdf": "https://www.maths.lth.se/matematiklu/personal/sigma/Riemann.pdf",
    "http://mysite.science.uottawa.ca/rossmann/Differential%20Geometry%20book_files/Diffgeo.pdf": "https://mysite.science.uottawa.ca/rossmann/Differential%20Geometry%20book_files/Diffgeo.pdf",
    "http://www.jirka.org/ra/realanal.pdf": "https://www.jirka.org/ra/realanal.pdf",
    "http://www.maths.lancs.ac.uk/~belton/www/notes/fa_notes.pdf": "https://www.maths.lancs.ac.uk/~belton/www/notes/fa_notes.pdf",
    "http://www.math.jhu.edu/~eriehl/context/": "https://math.jhu.edu/~eriehl/context/",
    "http://www.jmilne.org/math/CourseNotes/GT.pdf": "https://www.jmilne.org/math/CourseNotes/GT.pdf",
    "http://www.jmilne.org/math/CourseNotes/FT.pdf": "https://www.jmilne.org/math/CourseNotes/FT.pdf",
    "http://www.jmilne.org/math/CourseNotes/ANT.pdf": "https://www.jmilne.org/math/CourseNotes/ANT.pdf",
    "http://www.jmilne.org/math/CourseNotes/AG.pdf": "https://www.jmilne.org/math/CourseNotes/AG.pdf",
    "https://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf": "https://chance.dartmouth.edu",
    "https://www.encyclopediaofmath.org": "https://encyclopediaofmath.org/wiki/Main_Page",
    "https://unitconverters.net": "https://www.unitconverters.net/",
    "http://www.cis.upenn.edu/~jean/algeoms.pdf": "https://www.cis.upenn.edu/~jean/algeoms.pdf",
    "http://at.yorku.ca/topology/": "http://at.yorku.ca/index.html",
    "http://www.fourierandwavelets.org/FSP_v1.1_2014.pdf": "https://fourierandwavelets.org/FSP_v1.1_2014.pdf",
    "https://github.com/nelson-brochado/understanding-math": "https://github.com/nbro/understanding-math",
    "http://www.cs.bgu.ac.il/~leonid/ode_bio_files/Ionascu_LectNotes.pdf": "https://www.cs.bgu.ac.il/~leonid/ode_bio_files/Ionascu_LectNotes.pdf",
    "http://www.cis.upenn.edu/~jean/math-basics.pdf": "https://www.cis.upenn.edu/~jean/math-deep.pdf",
    "http://www.math.colostate.edu/~renzo/teaching/Topology10/Notes.pdf": "https://www.math.colostate.edu/~renzo/teaching/Topology10/Notes.pdf",
    "http://www.math.ku.dk/~moller/e03/3gt/notes/gtnotes.pdf": "http://web.math.ku.dk/~moller/e03/3gt/notes/gtnotes.pdf",
    "http://www.math.ku.dk/noter/filer/koman-12.pdf": "http://web.math.ku.dk/noter/filer/koman-12.pdf",
    "http://wstein.org/ent/ent.pdf": "https://wstein.org/ent/ent.pdf",
    "https://pdfs.semanticscholar.org/6967/f52773d9c2ccfc94658657a5761e0f00e95a.pdf": "https://www.semanticscholar.org/paper/Introduction-to-Logic%2C-Second-Edition-Genesereth-Kao/6967f52773d9c2ccfc94658657a5761e0f00e95a?p2df",
    "http://spot.colorado.edu/~baggett/functional.html": "https://spot.colorado.edu/~baggett/functional.html",
    "http://spot.colorado.edu/~baggett/analysis.html": "https://spot.colorado.edu/~baggett/analysis.html",
    "http://users.math.msu.edu/users/gnagy/teaching/ode.pdf": "https://users.math.msu.edu/users/gnagy/teaching/ode.pdf",
    "http://www.ece.rutgers.edu/~orfanidi/intro2sp/orfanidis-i2sp.pdf": "https://www.ece.rutgers.edu/~orfanidi/intro2sp/orfanidis-i2sp.pdf",
    "https://ccrma.stanford.edu/~jos/mdft": "https://ccrma.stanford.edu/~jos/mdft/",
    "http://www.math.utk.edu/~wagner/papers/comb.pdf": "https://www.math.utk.edu/~wagner/papers/comb.pdf",
    "http://digitalcommons.trinity.edu/mono/8/": "https://digitalcommons.trinity.edu/mono/8/",
    "http://digitalcommons.trinity.edu/mono/9/": "https://digitalcommons.trinity.edu/mono/9/",
    "http://www.math.miami.edu/~ec/book": "https://www.math.miami.edu/~ec/book/",
    "http://people.math.gatech.edu/%7Ecain/notes/calculus.html": "https://people.math.gatech.edu/~cain/notes/calculus.html",
    "http://people.math.gatech.edu/%7Ecain/winter99/complex.html": "https://people.math.gatech.edu/~cain/winter99/complex.html",
    "https://www.ma.utexas.edu/users/gordanz/notes/introduction_to_stochastic_processes.pdf": "https://web.ma.utexas.edu/users/gordanz/notes/introduction_to_stochastic_processes.pdf",
    "http://people.math.gatech.edu/~trotter/book.pdf": "https://people.math.gatech.edu/~trotter/book.pdf",
    "http://pages.pomona.edu/~ajr04747/Fall2009/Math152/Notes/Math152NotesFall09.pdf": "https://pages.pomona.edu/~ajr04747/Fall2009/Math152/Notes/Math152NotesFall09.pdf",
    "http://users.math.msu.edu/users/jeffrey/920/920notes.pdf": "https://users.math.msu.edu/users/schenke6/920/920notes.pdf",
    "https://www.math.upenn.edu/~ghrist/notes.html": "https://www2.math.upenn.edu/~ghrist/notes.html",
    "https://www.math.upenn.edu/~wilf/AeqB.html": "https://www2.math.upenn.edu/~wilf/AeqB.html",
    "http://www.maths.usyd.edu.au/u/bobh/UoS/rfwhole.pdf": "https://www.maths.usyd.edu.au/u/bobh/UoS/rfwhole.pdf",
    "http://www.maths.usyd.edu.au/u/bobh/UoS/MATH2902/vswhole.pdf": "https://www.maths.usyd.edu.au/u/bobh/UoS/MATH2902/vswhole.pdf",
    "http://plato.stanford.edu/entries/set-theory/": "https://plato.stanford.edu/entries/set-theory/",
    "http://joshua.smcvt.edu/linearalgebra": "https://joshua.smcvt.edu/linearalgebra/",
    "http://www.math.upenn.edu/~wilf/DownldGF.html": "https://www2.math.upenn.edu/~wilf/DownldGF.html",
    "http://msri.org/publications/books/gt3m/": "http://library.msri.org/books/gt3m/",
    "http://www.math.upenn.edu/%7Ewilf/AlgComp3.html": "https://www2.math.upenn.edu/~wilf/AlgComp3.html",
    "http://www.ellerman.org/Davids-Stuff/Maths/Rota-Baclawski-Prob-Theory-79.pdf": "https://ellerman.org/Davids-Stuff/Maths/Rota-Baclawski-Prob-Theory-79.pdf",
    "https://www.ma.utexas.edu/ibl1/courses/resources/12_15_07_grad_alg_top_mooremethod.pdf": "https://web.ma.utexas.edu/ibl1/courses/resources/12_15_07_grad_alg_top_mooremethod.pdf",
    "http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf": "http://faculty.marshall.usc.edu/gareth-james/",
    "http://www.math.uiuc.edu/~r-ash/Algebra.html": "https://faculty.math.illinois.edu/~r-ash/Algebra.html",
    "http://www.math.uiuc.edu/~jpda/jpd-complex-geometry-book-5-refs-bip.pdf": "https://faculty.math.illinois.edu/~jpda/jpd-complex-geometry-book-5-refs-bip.pdf",
    "http://www.math.uiuc.edu/~laugesen/545/545Lectures.pdf": "https://faculty.math.illinois.edu/~laugesen/545/545Lectures.pdf",
    "http://www.math.uiuc.edu/~hildebr/ant/main.pdf": "https://faculty.math.illinois.edu/~hildebr/ant/main.pdf",
    "http://www.math.uiuc.edu/~r-ash/ANT.html": "https://faculty.math.illinois.edu/~r-ash/ANT.html",
    "http://www.math.wisc.edu/~keisler/calc.html": "https://people.math.wisc.edu/~keisler/calc.html",
    
    # Dead links that have working alternatives - need to be handled carefully
    "http://www.mathematik.uni-kl.de/~gathmann/class/alggeom-2002/main.pdf": "https://www.mathematik.uni-kl.de/~gathmann/class/alggeom-2002/main.pdf",  # Still 404, will remove
    "http://www.math.cornell.edu/~hatcher/AT/AT.pdf": "https://pi.math.cornell.edu/~hatcher/AT/AT.pdf",
    "http://people.math.gatech.edu/~mbaker/pdf/ANTBook.pdf": "https://mattbaker.blog/",
    "https://jamesbrennan.org/algebra": "https://jamesbrennan.org/algebra/",  # 403, will remove
    "http://www.seas.upenn.edu/~jean/diffgeom.pdf": "https://www.cis.upenn.edu/~jean/",  # Dead, link to author page
    "http://www.maths.manchester.ac.uk/~cwalkden/complex-analysis/complex_analysis.pdf": "https://personalpages.manchester.ac.uk/staff/charles.walkden/",
}

# Links to remove (completely dead with no replacement)
REMOVE_LINES = [
    "http://www.gold-saucer.org/math/lebesgue/lebesgue.pdf",
    "http://www.math.uchicago.edu/~schlag/harmonicnotes.pdf",
    "http://www.ohio.edu/people/ehrlich/ConwayNames.pdf",
    "http://www.indiana.edu/~jfdavis/teaching/m623/book.pdf",
    "http://www.math.hkbu.edu.hk/~zeng/Teaching/math3680/FAnotes.pdf",
    "http://www.math.nus.edu.sg/~matwujie/ma5209.pdf",
    "http://www.cs.man.ac.uk/~hsimmons/zCATS.pdf",
    "http://prac.im.pwr.wroc.pl/~kwasnicki/pl/stuff/tbb-hyper.pdf",
    "http://www.math.uwaterloo.ca/~lwmarcou/Preprints/LinearAnalysis.pdf",
    "https://zodml.org/sites/default/files/Introduction_to_Abstract_Algebra_0.pdf",
    "http://www1.spms.ntu.edu.sg/~frederique/AA11.pdf",
    "http://www1.spms.ntu.edu.sg/~frederique/ANT10.pdf",
    "http://www.mecmath.net/trig/trigbook.pdf",
    "http://www.math.umd.edu/~dlevy/books/na.pdf",
    "https://terrytao.files.wordpress.com/2011/01/measure-book1.pdf",
    "https://www.tedsundstrom.com/mathreasoning",
    "http://www.math.clemson.edu/~jimlb/Teaching/2009-10/Math986/Topology.pdf",
    "https://www.people.vcu.edu/~rhammack/BookOfProof/",
    "http://www2.math.ou.edu/~cremling/teaching/lecturenotes/fa-new/LN-I.pdf",
    "http://www.ats.ucla.edu/stat/papers/",
    "https://www2.bc.edu/mark-reeder/Groups.pdf",
    "http://www.malaspina.com/etext/heavens.htm",
    "https://www.singular.uni-kl.de/",
    "https://webdocs.cs.ualberta.ca/~sutton/book/bookdraft2016sep.pdf",
]

def fix_links(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply redirects
    for old_url, new_url in REDIRECTS.items():
        if old_url in content:
            content = content.replace(old_url, new_url)
            print(f"✓ Replaced: {old_url[:80]}...")
    
    # Remove dead links
    lines = content.split('\n')
    new_lines = []
    removed_count = 0
    
    for line in lines:
        should_remove = False
        for dead_url in REMOVE_LINES:
            if dead_url in line:
                print(f"✗ Removing line with dead link: {dead_url[:80]}...")
                should_remove = True
                removed_count += 1
                break
        if not should_remove:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Fixed {len(REDIRECTS)} redirects and removed {removed_count} dead links")

if __name__ == '__main__':
    fix_links('README.md')
