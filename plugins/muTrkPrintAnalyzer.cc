#include "OSUT3Analysis/JoshAnalyzer/plugins/muTrkPrintAnalyzer.h"
#include "DataFormats/Math/interface/deltaR.h"

muTrkPrintAnalyzer::muTrkPrintAnalyzer(const edm::ParameterSet &cfg) : 
    collections_ (cfg.getParameter<edm::ParameterSet> ("collections"))
    //muonTag_ (cfg.getParameter<edm::InputTag> ("muons")),
    //trackTag_ (cfg.getParameter<edm::InputTag> ("tracks"))
{
    
    anatools::getAllTokens(collections_, consumesCollector(), tokens_);

    muonToken_ = consumes<vector<TYPE(muons)> > (muonTag_);
    trackToken_ = consumes<vector<TYPE(tracks)> > (trackTag_);
}


muTrkPrintAnalyzer::~muTrkPrintAnalyzer() { }

void muTrkPrintAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup) {

    anatools::getRequiredCollections(objectsToGet_, handles_, event, tokens_);

    edm::Handle <vector<TYPE(tracks)> > trackHandle;
    event.getByToken(trackToken_, trackHandle);

    edm::Handle <vector<TYPE(muons)> > muonHandle;
    event.getByToken(muonToken_, muonHandle);

    for (const auto &muon : *muonHandle) {
        
        std::cout << muon << std::endl;

    }

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(muTrkPrintAnalyzer);
