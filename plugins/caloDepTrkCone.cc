#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "OSUT3Analysis/JoshAnalyzer/plugins/caloDepTrkCone.h"
#include "DataFormats/Math/interface/deltaR.h"

caloDepTrkCone::caloDepTrkCone(const edm::ParameterSet &cfg) : EventVariableProducer(cfg) {
    //dRConeCut_ = cfg.getParameter<double>("dRConeCut");
    tokens_.clusterToken = consumes <vector<TYPE(superclusters)> > (collections_.getParameter<edm::InputTag> ("superclusters"));
    tokens_.trackToken = consumes <vector<TYPE(tracks)> > (collections_.getParameter<edm::InputTag> ("tracks"));
}

caloDepTrkCone::~caloDepTrkCone() { }

void caloDepTrkCone::AddVariables(const edm::Event &event) {

    edm::Handle <vector<TYPE(tracks)> > trackHandle;
    event.getByToken(tokens_.trackToken, trackHandle);

    edm::Handle <vector<TYPE(superclusters)> > clusterHandle;
    event.getByToken(tokens_.clusterToken, clusterHandle);

    double coneEdep = 0;
    for (const auto &track : *trackHandle) {
        for (const auto &cluster : *clusterHandle) {

            if (deltaR(track, cluster) < 0.3) {
                coneEdep += cluster.energy();
            }
        }
    }

    (*eventvariables)["caloDepTrkCone"] = coneEdep;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(caloDepTrkCone);
