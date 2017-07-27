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
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_201.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_202.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_203.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_204.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_205.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_206.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_207.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_208.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_209.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_210.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_211.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_212.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_213.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_214.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_215.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_216.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_217.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_218.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_219.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_220.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_221.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_222.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_223.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_224.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_225.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_226.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_227.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_228.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_229.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_230.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_231.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_232.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_233.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_234.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_235.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_236.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_237.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_238.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_239.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_240.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_241.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_242.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_243.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_244.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_245.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_246.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_247.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_248.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_249.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_250.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_251.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_252.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_253.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_254.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_255.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_256.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_257.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_258.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_259.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_260.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_261.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_262.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_263.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_264.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_265.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_266.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_267.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_268.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_269.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_270.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_271.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_272.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_273.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_274.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_275.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_276.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_277.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_278.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_279.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_280.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_281.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_282.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_283.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_284.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_285.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_286.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_287.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_288.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_289.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_290.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_291.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_292.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_293.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_294.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_295.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_296.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_297.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_298.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_299.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_300.root",

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
    fileName = cms.string("histoTracksDemo200.root")
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
