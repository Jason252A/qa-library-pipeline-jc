# Architecture Decision Record

# Medallion Architecture - Group 2
!!! Info "Test info"
!!! Notes "note info"
## heading 1
- bullet 1
- bullet 2

## Task

Create a Mermaid diagram showing how this pipeline should be organised into Bronze, Silver and Gold layers.

Your diagram should show:

- source data
- Bronze layer
- Silver layer
- Gold layer
- at least one data quality or validation step
- at least one final output for a user or stakeholder

## Diagram


```mermaid
flowchart LR
   
    
    subgraph SourceFile["Source Data"]
        catalogue[catalogue raw data]
        circulation_data[circulation raw data]
        events_data[events raw data]
        feedback[feedback raw data]
    end
    
    subgraph Bronze["Bronze Data"]
        cataloguebronze[catalogue data]
        circulation_databronze[circulation data]
        events_databronze[events data]
        feedbackbronze[feedback data]
    end
    
    catalogue --> Checkcata{Quality check}
    Checkcata -->|Pass| cataloguebronze
    Checkcata -->|Fail| Quarantine1[QuarantineCata]
    
    circulation_data --> Checkcirc{Quality check}
    Checkcirc -->|Pass| circulation_databronze
    Checkcirc -->|Fail| Quarantine2[QuarantineCirc]
    
    
    events_data --> events_databronze
    feedback --> feedbackbronze
    
    subgraph Silver["Silver Data"]
        cataloguesilver[catalogue clean data]
        circulation_datasilver[circulation clean data]
        events_datasilver[events clean data]
        feedbacksilver[feedback clean data]
    end
    
    cataloguebronze --> cataloguesilver
    circulation_databronze --> circulation_datasilver
    events_databronze --> events_datasilver
    feedbackbronze --> feedbacksilver
    
    subgraph Gold["Gold Data"]
    BookSaleEvent[Book Loan by event]

    end
    
    
    circulation_datasilver --> BookSaleEvent
    events_datasilver --> BookSaleEvent
    

    
```

## Questions to answer:

### One design decision
- We decided to...

### One question or risk
- We are unsure about...
