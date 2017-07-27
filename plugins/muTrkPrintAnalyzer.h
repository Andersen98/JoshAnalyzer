#ifndef MUTRKPRINTANALYZER
#define MUTRKPRINTANALYZER 

#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/Common/interface/Handle.h"
#include "OSUT3Analysis/AnaTools/interface/AnalysisTypes.h"

class muTrkPrintAnalyzer : public edm::EDAnalyzer {

    public:

        muTrkPrintAnalyzer(const edm::ParameterSet &);
        virtual ~muTrkPrintAnalyzer();

        void beginJob() {};
        void analyze(const edm::Event &, const edm::EventSetup &);
        void endJob() {};

    private:
        
        edm::ParameterSet collections_;
        Collections handles_;
        Tokens tokens_;

        unordered_set<string> objectsToGet_;

        edm::InputTag muonTag_;
        edm::InputTag trackTag_;

        edm::EDGetTokenT <vector<TYPE(tracks)> > trackToken_;
        edm::EDGetTokenT <vector<TYPE(muons)> > muonToken_;

};

#endif
