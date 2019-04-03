from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from data import data as y

plt.rcParams['text.latex.preamble'] = ['''
    \usepackage{lmodern}
    \usepackage{amsfonts}
''']

pp = PdfPages('../figures/exp_blockset_size.pdf')

rc('text', usetex=True)
rc(
    'font',
    family='serif',
    serif=['Computer Modern Roman'],
    monospace=['Computer Modern Typewriter'],
    size=27
)

MAX_X = 400

fig = plt.figure()
fig.set_size_inches(9, 9)

x = np.arange(1, MAX_X+1)
y = y[:MAX_X]
plt.plot(x, y, label='$\\mathbb{E}[B]$')
plt.plot(x, np.log2(x), '--', label='$lg(x)$')
plt.plot(x, np.log2(x) / 1.75, '--', label='$0.57 \\cdot lg(x)$')
plt.xlabel('Blockchain size')
plt.legend(loc='lower right')
# plt.show()

plt.savefig(pp, format='pdf', dpi=1000, bbox_inches='tight')

pp.close()
