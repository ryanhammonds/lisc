"""
Tutorial 01: Counts Collection
==============================

Collecting term co-occurrence data from scientific literature.
"""

###################################################################################################
# Term Co-occurrence
# ------------------
#
# The 'Counts' approach, or term co-occurrence searches the literature for
# how often terms of interest appear together.
#
# This type of analysis can be used to infer associations and relationships between terms.
#

###################################################################################################

from lisc import Counts
from lisc.utils.db import SCDB
from lisc.utils.io import save_object

###################################################################################################
# Counts Object
# -------------
#
# The :class:`~.Counts` object is used to handle term co-occurrence analyses.
#

###################################################################################################
# Counts: Single List of Terms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# For the first example of running a counts analysis, we will use a single list of terms.
#
# When a single list of terms is provided, the word co-occurrence is collected as the
# co-occurrence of each term with every other term in the list.
#
# Let's start with an example using different parts of the brain, and examine
# how often these brain regions are talked about together.
#

###################################################################################################

# Set up some terms to search for
terms = [['frontal lobe'], ['temporal lobe'], ['parietal lobe'], ['occipital lobe']]

# Initialize counts object & add the terms that we want to collect co-occurrences for
counts = Counts()
counts.add_terms(terms)

###################################################################################################

# Collect co-occurrence data
counts.run_collection(verbose=True)

###################################################################################################
#
# We have now collected some literature data!
#
# The :class:`~.Counts` object will now contain count data
# for the word co-occurrence data between terms.
#

###################################################################################################

# Check out the raw count data
print(counts.counts)

###################################################################################################
#
# The :class:`~.Counts` object also comes with some helper methods to explore the data.
#

###################################################################################################

# Check how many articles were found for each search term
counts.check_counts()

###################################################################################################

# Check the most studied term
counts.check_top()

###################################################################################################
# Counts: Two Terms Lists
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# In the first example above, we provided a single list of terms.
#
# Now let's explore using two different sets of terms.
#
# In this example, we will keep our list of brain regions, and explore how they
# relate to different sensory systems.
#

###################################################################################################

# Set some new terms
terms_a = [['frontal lobe'], ['temporal lobe'], ['parietal lobe'], ['occipital lobe']]
terms_b = [['vision'], ['audition', 'auditory'], ['somatosensory'], ['olfaction', 'smell'],
           ['gustation', 'taste'], ['proprioception'], ['nociception', 'pain']]

###################################################################################################

# Set terms lists
#  Different terms lists are indexed by the 'A' and 'B' labels
counts.add_terms(terms_a, dim='A')
counts.add_terms(terms_b, dim='B')

###################################################################################################

# Collect co-occurrence data
counts.run_collection()

###################################################################################################
#
# From there you can use all the same methods to explore the data we just collected.
#
# In the next tutorial, we explore analyzing our collected counts data.
#
# For now, let's save out our collected counts data, using the LISC utility to save the object.
#

###################################################################################################

# Save out the counts object
save_object(counts, 'tutorial_counts', directory=SCDB('lisc_db'))
