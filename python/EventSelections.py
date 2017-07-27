import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *
from DisappTrks.StandardAnalysis.utilities import *
from OSUT3Analysis.JoshAnalyzer.Cuts import *

################################################################################
#                              Basic Selection                                 #
################################################################################
basicSelection = cms.PSet(
    name = cms.string("basicSelection"),
    cuts = cms.VPSet (
        cutMuonPt20,
        cutMuonEta,
        cutTrkPt20,
        cutTrkEta,
        cutTrkEcalGap,
        cutTrkIsoP15,
        cutTrkMuonInvMassUpper,
        cutTrkMuonInvMassLower,
    )
)

################################################################################
#                           Missing Hits Selection                             #
################################################################################
trkZeroMissingHitsECalDep02 = cms.PSet(
    name = cms.string("trkZeroMissingHitsECalDep02"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkZeroMissingHits,
        cutTrkEcalDep02, 
    )
)

trkOneMissingHitsECalDep02 = cms.PSet(
    name = cms.string("trkOneMissingHitsECalDep02"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkOneMissingHits,
        cutTrkEcalDep02,
    )
)

trkTwoMissingHitsECalDep02 = cms.PSet(
    name = cms.string("trkTwoMissingHitsECalDep02"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkTwoMissingHits,
        cutTrkEcalDep02,
    )
)

trkThreeMissingHitsECalDep02 = cms.PSet(
    name = cms.string("trkThreeMissingHitsECalDep02"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkThreeMissingHits,
        cutTrkEcalDep02,
    )
)

trkZeroMissingHitsECalDep20 = cms.PSet(
    name = cms.string("trkZeroMissingHitsECalDep20"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkZeroMissingHits,
        cutTrkEcalDep20, 
    )
)

trkOneMissingHitsECalDep20 = cms.PSet(
    name = cms.string("trkOneMissingHitsECalDep20"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkOneMissingHits,
        cutTrkEcalDep20,
    )
)

trkTwoMissingHitsECalDep20 = cms.PSet(
    name = cms.string("trkTwoMissingHitsECalDep20"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkTwoMissingHits,
        cutTrkEcalDep20,
    )
)

trkThreeMissingHitsECalDep20 = cms.PSet(
    name = cms.string("trkThreeMissingHitsECalDep20"),
    cuts = basicSelection.cuts + cms.VPSet (
        cutTrkThreeMissingHits,
        cutTrkEcalDep20,
    )
)
