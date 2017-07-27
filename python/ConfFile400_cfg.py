import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap
from OSUT3Analysis.JoshAnalyzer.EventSelections import *
from OSUT3Analysis.JoshAnalyzer.HistogramDefinitions import *

process = cms.Process("demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag,"80X_mcRun2_asymptotic_2016_v3","")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append('DebugNotes')
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",

    fileNames = cms.untracked.vstring(
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_401.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_402.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_403.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_404.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_405.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_406.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_407.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_408.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_409.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_410.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_411.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_412.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_413.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_414.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_415.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_416.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_417.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_418.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_419.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_420.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_421.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_422.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_423.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_424.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_425.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_426.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_427.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_428.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_429.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_430.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_431.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_432.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_433.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_434.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_435.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_436.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_437.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_438.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_439.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_440.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_441.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_442.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_443.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_444.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_445.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_446.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_447.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_448.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_449.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_450.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_451.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_452.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_453.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_454.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_455.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_456.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_457.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_458.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_459.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_460.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_461.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_462.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_463.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_464.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_465.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_466.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_467.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_468.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_469.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_470.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_471.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_472.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_473.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_474.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_475.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_476.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_477.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_478.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_479.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_480.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_481.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_482.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_483.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_484.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_485.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_486.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_487.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_488.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_489.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_490.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_491.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_492.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_493.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_494.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_495.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_496.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_497.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_498.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_499.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_500.root",

    ),
)

weights = cms.VPSet (
#    cms.PSet (
#        inputCollections = cms.vstring("muons"),
#        inputVariable = cms.string("pt")
#    ),
#    cms.PSet (
#        inputCollections = cms.vstring("eventvariables"),
#        inputVariable = cms.string("muTrackInvMass"),
#    )
)

variableProducer = []
variableProducer.append("caloDepTrkCone")

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string("histoTracksDemo400.root")
)

histograms = cms.VPSet(
    muonPlots,
    trackPlots,
    evtVarPlots,
)

add_channels (process, [trkZeroMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkOneMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkTwoMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkThreeMissingHitsECalDep02], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkZeroMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkOneMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkTwoMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
add_channels (process, [trkThreeMissingHitsECalDep20], histograms, weights, [], collectionMap, variableProducer, False)
