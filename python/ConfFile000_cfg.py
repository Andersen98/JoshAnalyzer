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
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_1.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_2.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_3.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_4.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_5.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_6.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_7.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_8.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_9.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_10.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_11.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_12.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_13.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_14.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_15.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_16.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_17.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_18.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_19.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_20.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_21.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_22.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_23.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_24.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_25.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_26.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_27.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_28.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_29.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_30.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_31.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_32.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_33.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_34.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_35.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_36.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_37.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_38.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_39.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_40.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_41.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_42.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_43.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_44.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_45.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_46.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_47.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_48.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_49.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_50.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_51.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_52.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_53.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_54.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_55.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_56.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_57.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_58.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_59.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_60.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_61.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_62.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_63.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_64.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_65.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_66.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_67.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_68.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_69.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_70.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_71.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_72.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_73.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_74.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_75.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_76.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_77.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_78.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_79.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_80.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_81.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_82.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_83.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_84.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_85.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_86.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_87.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_88.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_89.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_90.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_91.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_92.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_93.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_94.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_95.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_96.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_97.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_98.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_99.root",
        "file:///uscms_data/d1/jhiltb/skim/2015/baseSkims/DYJetsToLL_50/MuonTagSkim/skim_100.root",

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
    fileName = cms.string("histoTracksDemo000.root")
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
