# Central Ops Chargeback Platform Strategy Prompt

## Role and Purpose

You are an expert architect for data platforms and internal financial-transparency systems. Create a **Central Ops Chargeback Platform Strategy & Approach** that serves as the strategic reference for downstream activities including:
- Detailed technical architecture design
- User story creation and backlog prioritization
- Technology selection and evaluation
- Implementation planning and phasing
- Risk management and mitigation strategies
- Chargeback policy design, dispute controls, and anti-gaming safeguards

This strategy bridges the chargeback business case with technical execution. It defines the high-level "what", "why", and strategic "how" for a centralised application-support chargeback platform: time-log ingestion, activity-level attribution, monthly chargeback generation, drill-down evidence, dispute handling, and a future driver-based allocation model.

## Context and Inputs

You have access to the following project context:

1. **Project context** (`docs/project-context/overview.md`)
   - Business objectives and success criteria
   - Current challenges and pain points
   - Expected business outcomes and KPIs
   - Stakeholder requirements

2. **Architecture overview** (`docs/architecture/overview.md`)
   - Batch ingestion of time logs and ticket exports (Excel/CSV uploads for the prototype)
   - Application, activity-type, team-member, and cost-centre master data
   - Monthly chargeback calculation with drill-down from invoice line to underlying time entries and tickets
   - Dispute workflow before invoicing, audit trail, and role-based access

3. **Business context from the stakeholder transcript** (`transcript.md`)
   - Incident management has been centralised: a central team (~50 support headcount) runs incident management for ~1,600 applications across ~20-30 platforms and ~4 cost centres.
   - Today's allocation is a flat cost-centre split that does not reflect actual consumption; the cost moved from application teams to central ops but the accounting does not show it.
   - Phase 1 is transparency: every hour of central-ops effort is attributable to a specific application, a specific activity type (deployment, bug fix, incident, other), and a specific consumer team, with an audit trail that survives challenge.
   - Phase 2 is driver-based optimisation (incident count, severity-weighted effort, MTTR contribution). The data model must support this from day one even if the UI does not expose it yet.
   - A minimum retainer / floor charge is required to cover the standing inventory of people, tooling, and offices.
   - Gaming is a known reputation risk: in quiet months, hours may drift onto whichever team already carries a bad name. Phase 1 does not solve this, but the design must not make it worse and must leave a clean forensic trail for Phase 2 controls.
   - Target state: chargeback to the business (business line), not cost centre.
   - The stakeholder does not need an operational view for himself; his KPI is transparency of the chargeback.

4. **Technology and delivery preferences**
   - GCP as the cloud provider.
   - Batch data ingestion (Excel/CSV uploads) for the prototype; keep it simple.
   - No AI/ML and no hardware or edge components in scope.
   - Standard business-hours availability; simple compliance, security, and privacy needs.

## Scope and Boundaries

**In Scope (Strategic):**
- Business requirement alignment and solution strategy
- High-level data architecture: ingestion, master data, attribution, chargeback calculation, reporting
- Strategic technology decisions (for example batch vs. streaming, Excel-upload vs. ticketing-tool integration, cost-centre vs. business-line roll-up)
- Data platform principles and design philosophy
- Core data, governance, security, and operations capabilities and their rationale
- Key architectural principles and patterns
- Implementation phasing and value delivery roadmap (Phase 1 transparency, Phase 2 driver-based)
- Major decision points, trade-offs, and alternatives
- Risk landscape and strategic mitigations (including gaming and dispute risk)

**Out of Scope (Tactical):**
- Detailed technical specifications or configurations
- Specific code implementations or scripts
- Detailed data models and schema definitions (come during architecture phase)
- Specific GCP resource naming conventions or sizing
- Detailed cost estimates or line-item pricing
- Operational runbooks or deployment procedures
- AI/ML, hardware, edge, or device capabilities (not part of this initiative)

## Deliverables

You will create **three interconnected strategic documents** that together provide a complete strategic foundation for the chargeback initiative. Each document should be comprehensive yet focused on its specific purpose. Treat any information not confirmed by the project context or transcript as an assumption or decision requiring validation; do not invent financial approvals, HR data availability, or ticketing-tool integration commitments.

### 1. Chargeback Platform Strategy
**File:** `docs/project-context/data-platform-strategy.md`

This is the primary strategic document that defines the "what" and "why" of the chargeback platform.

Create this document with the following structure:

#### 1.1 Executive Summary
- **Business Context**: Problem statement and current state recap (2-3 sentences: centralised ops, flat cost-centre allocation, no consumption visibility)
- **Strategic Vision**: Proposed solution approach and target state (3-4 sentences)
- **Expected Outcomes**: Key benefits and measurable business impacts
- **Strategic Bets**: 2-3 key decisions or directions that define this strategy

#### 1.2 Business Requirements & Strategic Response
For each business objective identified in the project context and transcript, provide:
- **Requirement ID & Statement**: Clear reference to the business requirement
- **Strategic Approach**: High-level solution strategy (2-4 sentences)
- **Key Capabilities**: Primary platform capabilities required (for example time-log ingestion, application master data, activity-type classification, chargeback calculation, drill-down evidence, dispute workflow, retainer floor)
- **Success Criteria**: How we'll measure that this requirement is met
- **Dependencies**: Other requirements or capabilities this depends on
- **Strategic Rationale**: Why this approach best serves business objectives (consider alternatives briefly)

Example format:
```
**REQ-001: Activity-Level Time Attribution**
- Strategic Approach: Ingest time logs at team-member, application, and activity-type granularity, validated against application master data, so every hour is attributable and auditable
- Key Capabilities: Batch ingestion, master-data validation, activity-type taxonomy, audit trail
- Success Criteria: 100% of logged support hours map to a valid application and activity type; unallocated time visible and quantified
- Dependencies: Application master data (REQ-002), time-log source availability
- Strategic Rationale: Batch Excel ingestion chosen over ticketing-tool integration because (1) the stakeholder's current source of truth is a spreadsheet, (2) it proves the model fastest, (3) tool integration can follow once transparency is trusted
```

#### 1.3 Data Platform Strategy
- **Data Architecture Pattern**: Describe the ingestion-to-reporting flow and how it separates source data, master data, attribution logic, chargeback calculation, and reporting.
  - Apply: zone-based layering (raw → cleansed → curated → consumption), single responsibility per layer.
- **Data Storage Strategy**: Where time logs, ticket references, application/cost-centre master data, chargeback results, dispute records, and audit evidence will be stored and why.
  - Consider: Hot/warm/cold data tiers based on access patterns; retention for audit challenge.
- **Data Integration Approach**: Batch ingestion (Excel/CSV uploads) for the prototype; a future path to ticketing-tool integration for actual consumed hours (the current tooling charges requested windows, not actual consumption).
  - Consider: Idempotency and reprocessability of monthly runs; late-arriving logs; restatement policy after disputes.
  - Apply: ELT over ETL where possible for flexibility.
- **Data Modeling Approach**: Business-aligned analytical models for chargeback reporting, plus a data model that supports Phase 2 consumption drivers (incident count, severity-weighted effort, MTTR contribution) from day one.
  - Consider: Query performance, business-user understanding, and change management.
  - Apply: Dimensional models for applications, cost centres, business lines, team members, activity types, and time.
- **Data Quality Strategy**: How data quality will be ensured.
  - Consider: Data quality dimensions (completeness, accuracy, consistency, timeliness).
  - Apply: Quality checks at ingestion (valid application, valid activity type, valid team member), transformation, and consumption layers; explicit unallocated-time handling.
- **Data Lineage & Observability**: How data flow and quality will be tracked.
  - Consider: End-to-end lineage from invoice line back to source time entries; monitoring and alerting on monthly runs.
- **Master Data Strategy**: Application-to-cost-centre-to-business-line hierarchy (~1,600 applications, ~4 cost centres), activity-type taxonomy (deployment, bug fix, incident, other), and change management for master data.
- **Chargeback Calculation Strategy**: How logged effort becomes a defensible bill — hourly rates or blended cost, retainer floor, roll-up to cost centre today and business line as target state, and the forensic trail that survives challenge from application owners, finance leads, and internal audit.
- **Anti-Gaming Design**: How the design avoids making gaming worse — immutable raw logs, drill-down evidence, unallocated-time visibility, and a clean forensic trail for Phase 2 controls.
- **Security & Governance Approach**: High-level security and compliance strategy.
  - Consider: Data classification, role-based access (central ops lead, application owners, finance owners, business-line owners), audit logging.
  - Apply: Principle of least privilege; sensitive HR cost data masked or restricted as needed.

#### 1.4 Technology Approach
Note: Keep this high-level. Specific services will be chosen during architecture phase.
- **Cloud Platform Rationale**: Explain why GCP fits the stated managed-service, simplicity, and operational needs, while marking service-availability verification and billing/landing-zone access as required validations.
  - Consider: Existing investments, team skills, cost model.
- **Core Platform Capabilities Needed**: File ingestion, storage, transformation, master-data management, calculation engine, reporting/BI, access control, and observability.
  - Consider: Managed services vs. self-managed (prefer managed for operational simplicity).
  - Apply: Cloud-native services that reduce undifferentiated heavy lifting.
- **Integration Patterns**: Batch file upload now; API or scheduled extraction from the ticketing tool later; API-first reporting for drill-down.
  - Consider: Loose coupling so the ingestion source can change without rewriting the calculation layer.
- **Analytics & Reporting Approach**: Governed monthly chargeback reports with drill-down from invoice line to time entries and tickets; dashboards for utilisation, unallocated time, and contested items.
  - Consider: Semantic layer for business logic, governed self-service.
  - Apply: Single version of truth through curated data products.
- **Infrastructure as Code**: How infrastructure will be defined and deployed.
  - Consider: Version control, repeatability, and environment parity.
  - Apply: Declarative infrastructure definitions (Terraform).

### 2. Value Delivery Roadmap
**File:** `docs/project-context/value-delivery-roadmap.md`

This document defines the strategic phasing and sequencing of value delivery - the "when" and "in what order".

Create this document with the following structure:

#### 2.1 Overview & Phasing Philosophy
- Brief summary of the overall delivery strategy
- Link to the main strategy document
- Explanation of phasing principles being applied

#### 2.2 Strategic Phasing Approach
Articulate the core principles guiding the phasing:
- **Value First**: Start with **high-value, low-complexity** use cases that prove platform value early (crawl-walk-run)
- **End-to-End**: Deliver **working vertical slices** rather than horizontal infrastructure layers
- **Foundation Early**: Include **observability, security, and governance** from Phase 1—technical debt is expensive
- **Learn and Adapt**: Early phases validate assumptions and inform later phases
- **Measurable Progress**: Each phase delivers **tangible business outcomes**, not just technical milestones

#### 2.3 Phase Definitions
Recommend 2-4 phases that progressively build capability while delivering business value. Anchor Phase 1 on the stakeholder's stated ask: transparency and a defensible monthly chargeback for the ~50-person support operation across ~1,600 applications and ~4 cost centres.

For each phase, provide:
- **Phase Name & Strategic Objectives**: What will be delivered and why
- **Key Capabilities**: Features and capabilities included in this phase
- **Business Value & Outcomes**: Specific measurable outcomes stakeholders will see (with metrics)
- **Strategic Enablers**: What this phase enables for future phases
- **Success Criteria**: How we'll know this phase is complete
- **Dependencies & Prerequisites**: What must be in place before starting
- **Estimated Timeline**: High-level timeframe

Example format:
```
### Phase 1: Transparency & Defensible Chargeback
**Strategic Objectives**: Prove where central-ops time went and turn it into a bill that survives challenge

**Key Capabilities**:
- Excel/CSV ingestion of time logs (team member, application, activity type, hours, ticket reference)
- Application and cost-centre master data (~1,600 applications, ~4 cost centres)
- Monthly chargeback calculation with retainer floor
- Drill-down from invoice line to time entries and tickets
- Dispute workflow before invoicing

**Business Value & Outcomes**:
- Replace flat cost-centre allocation with consumption-based chargeback
- Application owners can verify every billed hour ("$40,000 → these 320 entries against these 47 tickets")
- Unallocated time and contested items visible before month close
- KPI: 100% of logged hours attributable or explicitly flagged as unallocated

**Strategic Enablers**:
- Data model already captures Phase 2 drivers (incident count, severity, MTTR)
- Establishes trust required before driver-based allocation
- Proves GCP platform capabilities

**Success Criteria**:
- First monthly chargeback generated and accepted without material dispute
- Drill-down from every invoice line to source evidence
- Finance can reconcile chargeback into the ledger

**Dependencies & Prerequisites**:
- GCP project and access provisioned
- Sample time-log and master-data files agreed with the central-ops lead
- Rate/blended-cost basis for the retainer floor agreed with finance

**Estimated Timeline**: Weeks 1-6
```

#### 2.4 Cross-Phase Dependencies
Document major dependencies between phases:
- What must be completed in earlier phases for later phases to succeed (e.g., trust in Phase 1 evidence is a prerequisite for Phase 2 driver-based allocation)
- Key decision points that could alter the roadmap (e.g., ticketing-tool integration, business-line hierarchy availability)
- Parallel work streams that could accelerate delivery

#### 2.5 Value Milestones
Create a timeline view of key value milestones:
- When specific business capabilities will be available
- Major stakeholder demos or decision points
- Go-live dates for monthly chargeback cycles

### 3. Risk & Constraint Register
**File:** `docs/project-context/risk-constraint-register.md`

This document captures the risk landscape and boundary conditions for the strategy.

Create this document with the following structure:

#### 3.1 Overview
- Purpose of this register
- How risks will be monitored and managed
- Link to main strategy document

#### 3.2 Risk Register

Create a comprehensive risk register in table format:

| Risk ID | Risk Description | Likelihood | Impact | Mitigation Strategy | Owner Role | Phase Affected |
|---------|-----------------|------------|--------|---------------------|------------|----------------|
| R-001 | Time logs incomplete or misattributed at source | Medium | High | Ingestion validation, unallocated-time reporting, monthly quality checks | Data Engineer | Phase 1 |

Include risks related to:
- **Data quality and availability**: Manual Excel entry errors, missing ticket references, late-arriving logs, master-data staleness
- **Gaming and behavioural risk**: Hours drifting onto teams with a bad reputation in quiet months; pressure to "show productivity"; the design must not make this worse and must leave a forensic trail
- **Dispute and adoption risk**: Application owners challenging bills; finance rejecting the basis; chargeback losing credibility after one bad month
- **Technical complexity and skill gaps**: Team learning curve with GCP, new technology adoption
- **Timeline and resource constraints**: Scope creep, dependency delays, resource availability
- **Integration challenges**: Future ticketing-tool integration (current tooling tracks requested windows, not actual consumption), file format changes
- **Security and compliance concerns**: Sensitive cost/HR data access, privacy of team-member-level data
- **Scalability and performance**: Application-hierarchy growth, multi-month restatements
- **Vendor lock-in**: Over-reliance on proprietary services, migration complexity
- **Data drift**: Schema evolution in uploaded files, hierarchy changes (cost centre → business line)

For each risk, ensure:
- Clear, specific description
- Realistic likelihood (Low/Medium/High)
- Business impact assessment (Low/Medium/High/Critical)
- Actionable mitigation strategy
- Clear ownership
- Phase where risk is most relevant

#### 3.3 Assumptions

Clearly document assumptions about:
- **Project Scope**: What's included/excluded, boundaries (no AI/ML, no hardware; prototype uses Excel uploads)
- **Data Availability**: Time-log file availability and format stability, master-data accuracy, rate/blended-cost basis
- **Skills & Capabilities**: Team composition, skill levels, learning capacity
- **Timeline**: Project duration, phase lengths, resource availability
- **Technology**: GCP access, environment provisioning, tool availability
- **Organization**: Stakeholder engagement, decision-making speed, finance and application-owner participation in dispute cycles

Format:
```
**A-001**: Time-log Excel files are available monthly in a stable, agreed format
**A-002**: Team has access to a GCP project with appropriate permissions by Week 1
**A-003**: Business stakeholders available for monthly chargeback reviews and dispute cycles
```

#### 3.4 Constraints

Document known constraints that limit options or create boundaries:
- **Technical**: Batch-only ingestion for the prototype; no ticketing-tool API in Phase 1
- **Budget**: Cost limitations, resource constraints (if mentioned)
- **Regulatory**: Internal finance and audit requirements for chargeback evidence
- **Timeline**: Monthly close cycle as a hard delivery cadence
- **Organizational**: Existing cost-centre structure today; business-line hierarchy only in target state
- **Resource**: Team size, skill availability, concurrent project demands

Format:
```
**C-001**: Must use GCP as cloud provider
**C-002**: Phase 1 must use batch Excel/CSV uploads; no source-system integration
**C-003**: Chargeback must roll up to cost centres today, with business line as target state
```

#### 3.5 Risk Monitoring & Review
- How often risks will be reviewed
- Who is responsible for risk management
- Escalation process for high-impact risks
- Risk retirement criteria

## Chargeback Strategic Decision Framework

**Note**: This framework should be incorporated into **Document 1: Chargeback Platform Strategy** as the final section (1.5).

For major strategic decisions identified in the strategy, document:
- **Decision Point**: What strategic choice needs to be made
- **Options Considered**: 2-3 viable alternatives with pros/cons
- **Recommended Strategy**: Your strategic recommendation
- **Decision Criteria**: Business and technical factors that should drive the decision
- **Decision Timing**: What information or validation is needed before committing
- **Reversibility**: How easily this decision can be changed later (one-way vs. two-way door)

Example format:
```
### Decision D-001: Raw Hours vs. Driver-Based Allocation

**Decision Point**: What allocation basis should anchor the Phase 1 chargeback?

**Options Considered**:
1. **Raw logged hours**: Charge exactly what was logged per application
   - Pros: Simple, directly evidenced, easy to defend with drill-down
   - Cons: Exposed to logging behaviour and gaming in quiet months

2. **Driver-based allocation**: Allocate by incident count, severity-weighted effort, MTTR contribution
   - Pros: Harder to game, fairer reflection of consumption
   - Cons: Requires trusted baseline data and agreed driver weights that do not exist yet

3. **Hybrid with retainer floor**: Raw hours plus a minimum retainer charge
   - Pros: Covers standing capacity, keeps evidence simple, dampens gaming incentives
   - Cons: Retainer basis must be agreed with finance

**Recommended Strategy**: Phase 1 uses raw logged hours plus a minimum retainer floor, with an immutable forensic trail. Phase 2 moves to driver-based allocation once transparency is live and trusted.

**Decision Criteria**:
- Survivability of challenge from application owners, finance leads, and internal audit
- Gaming resistance and behavioural incentives
- Availability and quality of driver data (incident counts, severity, MTTR)

**Decision Timing**: Retainer basis agreed with finance before the first monthly cycle; driver weights validated during Phase 1 data collection.

**Reversibility**: Two-way door. The data model captures drivers from day one, so the allocation basis can evolve without re-platforming.
```

## Strategic Principles to Guide Your Strategy

When developing your strategy and approach, ensure alignment with these core data platform principles:

### Architectural Principles
- **Layered Data Refinement**: Establish clear zones for progressive data quality improvement (e.g., raw → cleansed → curated)
- **Preserve the Past**: Retain source time logs in their original form; enable reprocessing, restatement, and historical analysis
- **Design for Change**: Anticipate schema evolution, hierarchy changes (cost centre → business line), and Phase 2 driver requirements without breaking existing consumers
- **Repeatability & Reliability**: Ensure monthly chargeback runs are deterministic and can be safely re-executed
- **Evidence by Design**: Every invoice line must drill down to its underlying time entries and ticket references; the audit trail must survive challenge

### Strategic Patterns
- **Choose the Right Pattern**: Select architectural patterns based on organizational structure, data volumes, and team capabilities
- **Minimize Complexity**: Start with simpler patterns (batch uploads, managed services); evolve only when requirements clearly justify additional complexity
- **Crawl-Walk-Run**: Excel prototype first, ticketing-tool integration later, driver-based allocation last

### Operational Foundation
- **Built-in Observability**: Plan for monitoring, alerting, and troubleshooting from day one—not as an afterthought
- **Data Quality by Design**: Embed quality validation throughout the data flow; fail fast to prevent bad data reaching an invoice
- **Cost-Conscious**: Consider data lifecycle management and compute efficiency in the approach
- **Testability**: Design for automated testing at each layer—data pipelines are code and deserve software engineering rigor

### Governance & Trust
- **Discoverable Data**: Plan for data cataloging and metadata management to enable self-service analytics
- **Security by Default**: Apply least-privilege access, data classification, and audit logging as foundational requirements
- **Lineage & Transparency**: Enable application owners and finance to understand data origins, transformations, and quality for informed decisions

### Scalability Considerations
- **Scale Up and Out**: Design for both increasing data volumes (multi-month history) and growing number of consumers (application owners, finance, business lines)
- **Performance Patterns**: Consider partitioning strategies and incremental processing appropriate to monthly query patterns
- **Avoid Premature Optimization**: Focus on critical paths; don't over-engineer for theoretical scale problems

## Quality Criteria

A high-quality Chargeback Platform Strategy & Approach document should:

✅ **Business-Aligned** - Every business requirement has a clear strategic response
✅ **Strategic Yet Actionable** - Provides clear direction without prescribing detailed implementation
✅ **Well-Justified** - Includes clear rationale linking business needs to technical approach
✅ **Trade-off Aware** - Shows consideration of alternatives and explicit decision-making
✅ **Appropriately Abstract** - Focuses on capabilities and patterns over specific tools (some specificity is OK given constraints)
✅ **Realistic & Pragmatic** - Considers organizational capabilities, constraints, and maturity
✅ **Value-Sequenced** - Shows logical implementation phases with clear business value
✅ **Risk-Conscious** - Identifies strategic risks, dependencies, and mitigation approaches (especially gaming and dispute risk)
✅ **Enables Downstream Work** - Provides sufficient foundation for architecture design and story writing
✅ **Principle-Based** - Applies relevant industry patterns and architectural principles
✅ **Future-Oriented** - Considers evolution to driver-based allocation and business-line chargeback
✅ **Decision-Transparent** - Documents key strategic decisions, alternatives considered, and rationale

## Output Format

Provide your response as **three separate, well-structured markdown documents**:

1. **`docs/project-context/data-platform-strategy.md`** - Primary Chargeback Platform Strategy (3,000-4,000 words)
2. **`docs/project-context/value-delivery-roadmap.md`** - Phasing and value delivery (1,500-2,500 words)
3. **`docs/project-context/risk-constraint-register.md`** - Risk and constraints (1,000-1,500 words)

### Document Requirements

Each document should be:
- **Comprehensive yet concise** - Cover all required elements without unnecessary detail
- **Scannable** - Use clear headings, bullets, and tables for easy navigation
- **Professional** - Written for technical and business stakeholders alike
- **Referenceable** - Each section should stand alone and be easily cited in downstream documents
- **Cross-linked** - Reference other documents where appropriate (e.g., "See Value Delivery Roadmap for phasing details")

### Presentation Format

Present your response as follows:

```markdown
# Document 1: Chargeback Platform Strategy

[Full content of data-platform-strategy.md]

---

# Document 2: Value Delivery Roadmap

[Full content of value-delivery-roadmap.md]

---

# Document 3: Risk & Constraint Register

[Full content of risk-constraint-register.md]
```

Each document should be complete and ready to save directly to its respective file path.