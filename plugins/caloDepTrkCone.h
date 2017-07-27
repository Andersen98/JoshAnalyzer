#ifndef VARIABLE_PRODUCER
#define VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

struct OriginalTokens
{
    edm::EDGetTokenT <vector<TYPE(superclusters)> > clusterToken;
    edm::EDGetTokenT <vector<TYPE(tracks)> > trackToken;
};

class caloDepTrkCone : public EventVariableProducer {

    public:

        caloDepTrkCone(const edm::ParameterSet &);
        ~caloDepTrkCone();
        OriginalTokens tokens_;

    private:

        void AddVariables(const edm::Event &);
};

#endif
