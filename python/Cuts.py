import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

################################################################################
#                                Basic Cuts                                    #
################################################################################

cutMuonPt20 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
)
cutMuonEta = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
)
cutTrkPt20 = cms.PSet (
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
)
cutTrkEta = cms.PSet (
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
)
cutTrkEcalGap = cms.PSet ( 
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.42 || fabs ( eta ) > 1.65"),
    numberRequired = cms.string(">= 1"),
)
cutTrkIsoP15 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("( trackIsoNoPUDRp3 / pt ) < 0.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMuonInvMassUpper = cms.PSet (
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string(invMassWithMuon ( "muon" ) + " < 100"),
    numberRequired = cms.string(">= 1")
)
cutTrkMuonInvMassLower = cms.PSet (
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string(invMassWithMuon ( "muon" ) + " > 80"),
    numberRequired = cms.string(">= 1")
)

################################################################################
#                             Missing Hits Cuts                                #
################################################################################

cutTrkZeroMissingHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkOneMissingHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits == 1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTwoMissingHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits == 2"),
    numberRequired = cms.string(">= 1"),
)
cutTrkThreeMissingHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits == 3"),
    numberRequired = cms.string(">= 1"),
)

################################################################################
#                            Track ECal Dep Cuts                               #
################################################################################

cutTrkEcalDep02 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloEMDRp3 <= 2.0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcalDep20 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloEMDRp3 >= 20"),
    numberRequired = cms.string(">= 1"),
)
