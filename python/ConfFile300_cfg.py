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
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_301.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_302.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_303.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_304.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_305.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_306.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_307.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_308.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_309.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_310.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_311.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_312.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_313.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_314.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_315.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_316.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_317.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_318.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_319.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_320.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_321.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_322.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_323.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_324.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_325.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_326.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_327.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_328.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_329.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_330.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_331.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_332.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_333.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_334.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_335.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_336.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_337.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_338.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_339.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_340.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_341.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_342.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_343.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_344.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_345.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_346.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_347.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_348.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_349.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_350.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_351.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_352.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_353.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_354.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_355.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_356.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_357.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_358.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_359.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_360.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_361.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_362.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_363.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_364.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_365.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_366.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_367.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_368.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_369.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_370.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_371.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_372.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_373.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_374.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_375.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_376.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_377.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_378.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_379.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_380.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_381.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_382.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_383.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_384.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_385.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_386.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_387.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_388.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_389.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_390.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_391.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_392.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_393.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_394.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_395.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_396.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_397.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_398.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_399.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_400.root",

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
    fileName = cms.string("histoTracksDemo300.root")
)

histograms = cms.VPSet(
    muonPlots,
    trackPlots,
    massPlot,
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
