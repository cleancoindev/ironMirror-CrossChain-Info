# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='ironMirror Cross Chain Monitoring Hub', page_icon=':bar_chart:', layout='wide')

# Title
st.title('ironMirror Cross Chain Monitoring Hub')

# Content
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 = st.columns(14)
c1.image(Image.open('images/ethereum-logo.png'))
c2.image(Image.open('images/bsc-logo.png'))
c3.image(Image.open('images/polygon-logo.png'))
c4.image(Image.open('images/solana-logo.png'))
c5.image(Image.open('images/avalanche-logo.png'))
c6.image(Image.open('images/cosmos-logo.png'))
c7.image(Image.open('images/near-logo.png'))
c8.image(Image.open('images/flow-logo.png'))
c9.image(Image.open('images/thorchain-logo.png'))
c10.image(Image.open('images/osmosis-logo.png'))
c11.image(Image.open('images/gnosis-logo.png'))
c12.image(Image.open('images/optimism-logo.png'))
c13.image(Image.open('images/arbitrum-logo.png'))
c14.image(Image.open('images/axelar-logo.png'))

st.write(
    """
    This ironMirror Analytics Tool for Users is here for your viewing needs and pleasure.

    The crypto industry continues to progress and its development has never stopped. Contributors
    of each blockchain keep developing each segment of the industry and the whole crypto ecosystem.
    This tool is designed to allow viewers to journey into the world of crypto ecosystems of some
    of the major blockchains, and compare their performance.

    This tool is designed and structured in multiple **Pages** that are accessible using the sidebar.
    Each of these Pages addresses a different segment of the crypto industry. Within each segment
    (Macro, Transfers, Swaps, NFTs, etc.) you are able to filter your desired blockchains to
    narrow/expand the comparison. By selecting a single blockchain, you can observe a deep dive
    into that particular network.

    All values for amounts, prices, and volumes are in **U.S. dollars** and the time frequency of the
    analysis was limited to the last **30 days**.
    """
)

st.subheader('Methodology')
st.write(
    """
    The data for this cross-chain comparison were selected via
    data platform by using its **REST API**. These queries are currently set to **re-run every 24 hours** to cover the latest
    data and are imported as a JSON file directly to each page. The data were selected with a **1 day delay** for all
    blockchains to be in sync with one another.

    It is worth mentioning that a considerable portion of the data used for this tool was manually decoded from the raw
    transaction data on some of the blockchains. Besides that, the names of addresses, DEXs, collections, etc. are also
    manually labeled. As the queries are updated on a daily basis to cover the most recent data, there is a chance
    that viewers encounter inconsistent data through the app. Due to the heavy computational power required to execute
    the queries, and also the size of the raw data being too large, it was not feasible to cover data for a longer period,
    or by downloading the data and loading it from the repository itself. Therefore, the REST API was selected as the
    proper form of loading data for the time being.
    """
)

st.subheader('Future Works')
st.write(
    """
To come:  Roadmap, NFTs for only ecosystem token sales, airdrops to the lost IRON value community that registered in the Titan Community discord form, 
a video game dev studio that has risen from the ashes....and much much more!  

Stay tuned here for details as we will also be beginning the Newsletter soon!
    """
)
