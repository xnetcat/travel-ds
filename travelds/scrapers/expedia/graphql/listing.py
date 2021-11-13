LISTING_QUERY = """
query PropertyOffers(
	$context: ContextInput!
	$propertyId: String!
	$searchCriteria: PropertySearchCriteriaInput
	$shoppingContext: ShoppingContextInput
	$travelAdTrackingInfo: PropertyTravelAdTrackingInfoInput
	$searchOffer: SearchOfferInput
	$referrer: String
) {
	propertyOffers(
		context: $context
		propertyId: $propertyId
		searchCriteria: $searchCriteria
		shoppingContext: $shoppingContext
		travelAdTrackingInfo: $travelAdTrackingInfo
		searchOffer: $searchOffer
		referrer: $referrer
	) {
		propertyHighlightSection {
			label
			header {
				badge {
					icon_temp {
						id
					}
					theme_temp
					theme
					text
				}
				mark {
					id
					description
				}
			}
			subSections {
				description
				contents {
					icon {
						id
						withBackground
						description
					}
					value
				}
			}
			footerLink {
				icon {
					id
				}
				link {
					referrerId
					uri {
						relativePath
						value
					}
					target
				}
				value
			}
		}
		propertySearchLink {
			icon {
				id
			}
			link {
				clientSideAnalytics {
					referrerId
					linkName
				}
				uri {
					relativePath
					value
				}
				referrerId
			}
			value
		}
		partnerPropertySearchLink {
			icon {
				id
			}
			link {
				uri {
					relativePath
					value
				}
				referrerId
			}
			value
		}
		filterPills {
			pillLabel
			type
			value
			state
			query
		}
		loading {
			accessibilityLabel
		}
		listingsHeader {
			text
		}
		searchCriteria {
			primary {
				dateRange {
					checkInDate {
						...DateFragment
					}
					checkOutDate {
						...DateFragment
					}
				}
				destination {
					regionId
				}
				rooms {
					adults
					children {
						age
					}
				}
			}
			secondary {
				booleans {
					id
					value
				}
				counts {
					id
					value
				}
				dates {
					id
					value {
						isoFormat
					}
				}
				ranges {
					id
					min
					max
				}
				selections {
					id
					value
				}
			}
		}
		tripSummary {
			...TripSummaryFragment
		}
		listings {
			...UnitFragment
		}
		categorizedListings {
			...CategorizedUnitFragment
			...MessageFragment
		}
		errorMessage {
			title {
				text
			}
			action {
				primary {
					text
					linkUrl
				}
			}
		}
		paymentPolicy {
			...PaymentPolicyFragment
		}
		serpMetadata {
			priceRange {
				value
			}
			priceRating {
				value
			}
		}
		soldOut
		stickyBar {
			displayPrice
			qualifier
			subText
			stickyButton {
				text
				targetRef
			}
			price {
				leadingCaption
				displayPrice {
					formatted
				}
				disclaimer {
					value
				}
			}
		}
		toastMessage {
			value
		}
		loyaltyDiscount {
			saveWithPointsMessage
			saveWithPointsActionMessage
		}
		legalDisclaimer {
			content {
				markupType
				text
			}
		}
		propertyLevelOffersMessage {
			...MessageFragment
		}
		offerLevelMessages {
			...MessageFragment
		}
		alternateDates {
			...AlternateDatesFragment
		}
		shoppingContext {
			multiItem {
				id
				packageType
			}
		}
		singleUnitOffer {
			...SingleOfferFragment
		}
		singleUnitOfferDialog {
			content {
				...SingleOfferFragment
			}
			toolbar {
				...LodgingDialogToolbarFragment
			}
			trigger {
				...LodgingDialogTriggerMessageFragment
			}
		}
		spaceDetails {
			header {
				text
				subText
			}
			floorPlan {
				images {
					alt
					image {
						description
						url
					}
					subjectId
				}
				toolbar {
					...LodgingDialogToolbarFragment
				}
				trigger {
					...LodgingDialogTriggerMessageFragment
				}
			}
			spaces {
				name
				description
				icons {
					...IconFragment
				}
			}
			summary
		}
	}
}
fragment AlternateDatesFragment on AlternateDatesCard {
	header {
		text
		subText
	}
	options {
		...AlternateDateOptionFragment
	}
}
fragment PropertyUnitDetailsDialog on PropertyUnitDetailsDialog {
	content {
		ratePlanTitle {
			text
		}
		details {
			header {
				text
				subText
			}
			contents {
				heading
				items {
					text
				}
			}
		}
	}
	trigger {
		value
		clientSideAnalytics {
			referrerId
			linkName
		}
		dialogTrigger {
			clientSideAnalytics {
				referrerId
			}
		}
	}
	toolbar {
		title
		icon {
			description
		}
		clientSideAnalytics {
			referrerId
			linkName
		}
	}
}
fragment MessageFragment on MessageResult {
	__typename
	type
	title {
		...TitleFragment
	}
	subtitle {
		...TitleFragment
	}
	action {
		primary {
			...ActionFragment
		}
		secondary {
			...ActionFragment
		}
	}
	featuredImage {
		url
		description
	}
}
fragment TitleFragment on MessagingResultTitle {
	text
	theme
	icon {
		...IconFragment
	}
	mark {
		id
		description
	}
	illustration {
		assetUri {
			value
		}
		description
	}
}
fragment ActionFragment on MessagingAction {
	linkUrl
	text
	referrerId
	actionDetails {
		name
		details
		title
		accessibilityLabel
		action
	}
	icon {
		id
	}
}
fragment LodgingNotificationsCardFragment on LodgingNotificationsCard {
	header {
		text
	}
	messages {
		...LodgingEnrichedMessageFragment
	}
}
fragment UnitCategorizationSelectionFragment on LodgingOfferOption {
	description
	subText
	enabled
	price
	optionId
	clientSideAnalytics {
		...ClientSideAnalyticsFragment
	}
	dialog {
		...LodgingPlainDialogFragment
	}
}
fragment UnitCategorizationHeaderFragment on LodgingOfferSelectionHeader {
	dialog {
		content {
			content
			title {
				text
				subText
			}
		}
		primaryUIButton {
			...UIPrimaryButtonFragment
		}
		toolbar {
			...LodgingDialogToolbarFragment
		}
		trigger {
			...LodgingDialogTriggerMessageFragment
		}
	}
	title {
		text
	}
}
fragment CategorizedUnitFragment on LodgingCategorizedUnit {
	__typename
	label
	header {
		text
	}
	highlightedMessages {
		...CancellationPolicyFragment
	}
	features {
		text
		moreInfo
		graphic {
			__typename
			... on Icon {
				...IconFragment
			}
			... on Mark {
				description
				id
			}
		}
		graphic {
			__typename
			...IconFragment
			...MarkFragment
		}
		moreInfoDialog {
			...LodgingPlainFullscreenDialogFragment
		}
	}
	primaryHeader {
		...UnitCategorizationHeaderFragment
	}
	secondaryHeader {
		...UnitCategorizationHeaderFragment
	}
	tertiaryHeader {
		...UnitCategorizationHeaderFragment
	}
	primarySelections {
		primarySelection {
			...UnitCategorizationSelectionFragment
		}
		secondarySelections {
			recommendedSelection
			secondarySelection {
				...UnitCategorizationSelectionFragment
			}
			tertiarySelections {
				...UnitCategorizationSelectionFragment
			}
		}
		propertyUnit {
			__typename
			id
			unitGallery {
				accessibilityLabel
				label
				images {
					image {
						description
						url
					}
				}
			}
			availabilityCallToAction {
				__typename
				... on LodgingPlainMessage {
					value
				}
				... on LodgingButton {
					text
				}
			}
			detailsDialog {
				...PropertyUnitDetailsDialog
			}
			roomAmenities {
				header {
					text
				}
				bodySubSections {
					contents {
						header {
							icon {
								id
							}
							text
						}
						items {
							... on PropertyContentItemMarkup {
								content {
									text
								}
							}
						}
					}
				}
			}
			ratePlans {
				...RatePlanFragment
			}
		}
	}
}
fragment UnitFragment on PropertyUnit {
	__typename
	bedOptions {
		name
		icon
	}
	id
	name
	header {
		icon {
			...IconFragment
		}
		text
		subText
	}
	detailsDialog {
		...PropertyUnitDetailsDialog
	}
	ratePlans {
		...RatePlanFragment
	}
	unavailableRatePlans {
		...RatePlanFragment
	}
	ratePlansExpando {
		expandButton {
			text
		}
	}
	features {
		text
		moreInfo
		graphic {
			__typename
			... on Icon {
				...IconFragment
			}
			... on Mark {
				description
				id
			}
		}
		graphic {
			__typename
			...IconFragment
			...MarkFragment
		}
		moreInfoDialog {
			...LodgingPlainFullscreenDialogFragment
		}
	}
	spaceDetails {
		header {
			text
			subText
		}
		floorPlan {
			images {
				alt
				image {
					description
					url
				}
				subjectId
			}
			toolbar {
				...LodgingDialogToolbarFragment
			}
			trigger {
				...LodgingDialogTriggerMessageFragment
			}
		}
		spaces {
			name
			description
			icons {
				...IconFragment
			}
		}
		summary
	}
	roomAmenities {
		header {
			text
		}
		bodySubSections {
			contents {
				header {
					text
					icon {
						id
					}
				}
				items {
					... on PropertyContentItemMarkup {
						content {
							text
						}
					}
				}
			}
		}
	}
	unitGallery {
		images {
			alt
			image {
				description
				url
			}
			thumbnail {
				description
				url
			}
			fallbackImage {
				description
				url
			}
			subjectId
		}
		accessibilityLabel
	}
	availabilityCallToAction {
		__typename
		... on LodgingPlainMessage {
			value
		}
		... on LodgingButton {
			text
		}
	}
}
fragment CancellationPolicyFragment on RatePlanMessage {
	__typename
	...LodgingPlainDialogFragment
	...LodgingEnrichedMessageFragment
}
fragment DateFragment on Date {
	month
	day
	year
	shortDateFormat
}
fragment RatePlanFragment on RatePlan {
	id
	name
	description
	loyaltyMessage {
		value
		state
		mark {
			id
		}
		egdsMark {
			url {
				value
			}
		}
		label
	}
	headerMessage {
		value
		subText
		theme
		label
	}
	priceDetails {
		...PriceDetailsFragment
	}
	amenities {
		id
		additionalInformation
		category
		description
		icon {
			id
			description
			size
		}
	}
	marketingSection {
		...MarketingSectionFragment
	}
	offerNotifications {
		...LodgingNotificationsCardFragment
	}
	highlightedMessages {
		...LodgingEnrichedMessageFragment
		...LodgingPlainMessageFragment
		...LodgingPlainDialogFragment
	}
	marketingChannelMessage {
		value
		mark {
			id
		}
	}
	badge {
		text
		theme_temp
		icon_temp {
			id
			description
			size
		}
	}
	etpDialogTopMessage {
		...MessageFragment
	}
	paymentPolicy {
		...PaymentPolicyFragment
	}
	reserveCallToAction {
		__typename
		... on EtpDialog {
			trigger {
				value
			}
			toolbar {
				icon {
					description
				}
				title
			}
		}
		... on LodgingForm {
			action
			inputs {
				... on LodgingTextInput {
					name
					type
					value
				}
			}
			method
			submit {
				text
			}
		}
	}
	shareUrl {
		accessibilityLabel
		link {
			uri {
				relativePath
			}
		}
		value
	}
}
fragment PriceDetailsFragment on Offer {
	optionTitle {
		text
	}
	availability {
		available
		text
		theme
		scarcityMessage
	}
	price {
		...PriceDisplayFragment
		options {
			...OptionFragment
		}
		priceMessaging {
			value
			theme
		}
		lead {
			formatted
		}
		disclaimer {
			value
		}
		roomNightMessage
		strikeOut {
			formatted
		}
		strikeOutType
		marketingFeeDetails {
			tierName
			tierIcon
			marketingFeeMessage {
				value
			}
		}
		multiItemPriceToken
	}
	cancellationPolicy {
		type
		text
		cancellationWindow {
			day
			month
			year
			hour
			minute
			second
			timeZoneOffsetSeconds
			fullDateFormat
		}
	}
	...PricePresentationDialogFragment
	priceBreakDownSummary {
		priceSummaryHeading {
			...LodgingEnrichedMessageFragment
		}
		sections {
			sectionHeading {
				...LodgingEnrichedMessageFragment
			}
			items {
				name {
					primaryMessage {
						...LodgingEnrichedMessageFragment
					}
					secondaryMessages {
						...LodgingEnrichedMessageFragment
					}
				}
				value {
					primaryMessage {
						...LodgingEnrichedMessageFragment
					}
					secondaryMessages {
						...LodgingEnrichedMessageFragment
					}
				}
			}
			sectionFooter {
				footerHeading {
					...LodgingEnrichedMessageFragment
				}
				footerMessages {
					...LodgingEnrichedMessageFragment
				}
			}
		}
		disclaimers {
			...LodgingEnrichedMessageFragment
		}
	}
	pointsApplied
	dataAttributes {
		key
		value
	}
	feeMessages {
		value
	}
	loyaltyMessage {
		state
		value
	}
	offerBookButton {
		action
		inputs {
			...LodgingTextInput
		}
		method
		submit {
			...ButtonFragment
		}
	}
	paymentModel
	noCreditCard
	installmentPayable
	totalPriceMessage
	deposit {
		...MoneyFragment
	}
	hotelCollect
	etpModalPolicies
	propertyNaturalKeys {
		...PropertyNaturalKeyFragment
	}
}
fragment PropertyNaturalKeyFragment on PropertyNaturalKey {
	id
	checkIn {
		...DateFragment
	}
	checkOut {
		...DateFragment
	}
	inventoryType
	noCreditCard
	ratePlanId
	ratePlanType
	roomTypeId
	rooms {
		childAges
		numberOfAdults
	}
	shoppingPath
}
fragment ButtonFragment on LodgingButton {
	text
	analytics {
		linkName
		referrerId
	}
}
fragment IconFragment on Icon {
	description
	id
	size
}
fragment MarkFragment on Mark {
	id
	description
}
fragment MarketingSectionFragment on MarketingSection {
	title {
		text
	}
	feeDetails {
		formattedFee
		marketingFeeMessage {
			value
		}
		mark {
			id
		}
		tierName
		tierMessage {
			value
			icon {
				id
				description
				size
			}
			mark {
				id
			}
		}
	}
	feeDialog {
		title
		content
		tertiaryUIButton {
			primary
		}
		trigger {
			value
			mark {
				id
			}
			icon {
				id
				size
			}
			clientSideAnalytics {
				linkName
				referrerId
			}
		}
	}
	paymentDetails {
		icon {
			id
		}
		value
	}
}
fragment LodgingTextInput on LodgingTextInput {
	name
	type
	value
}
fragment PaymentPolicyFragment on PropertyPaymentPolicyInfo {
	__typename
	paymentType
	heading
	descriptions {
		heading
		items {
			text
		}
	}
}
fragment OptionFragment on PropertyPriceOption {
	disclaimer {
		...LodgingPlainMessageFragment
	}
	priceDisclaimer {
		...LodgingPlainDialogFragment
	}
	displayPrice {
		...MoneyFragment
	}
	leadingCaption
	loyaltyPrice {
		amount {
			formatted
			raw
		}
		totalStrikeOutPoints {
			formatted
		}
		unit
	}
	strikeOut {
		...MoneyFragment
	}
	accessibilityLabel
}
fragment LodgingEnrichedMessageFragment on LodgingEnrichedMessage {
	__typename
	icon {
		id
		description
		size
	}
	label
	mark {
		id
		description
	}
	theme
	subText
	value
}
fragment LodgingPlainMessageFragment on LodgingPlainMessage {
	__typename
	value
}
fragment LodgingPlainDialogFragment on LodgingPlainDialog {
	__typename
	content
	primaryButton {
		...ButtonFragment
	}
	secondaryButton {
		...ButtonFragment
	}
	tertiaryButton {
		...ButtonFragment
	}
	primaryUIButton {
		...UIPrimaryButtonFragment
	}
	secondaryUIButton {
		primary
	}
	title
	toolbar {
		...LodgingDialogToolbarFragment
	}
	trigger {
		...LodgingDialogTriggerMessageFragment
	}
}
fragment UIPrimaryButtonFragment on UIPrimaryButton {
	__typename
	action {
		__typename
		analytics {
			__typename
			linkName
			referrerId
		}
		... on UILinkAction {
			__typename
			resource {
				__typename
				value
			}
		}
	}
	primary
}
fragment LodgingPlainFullscreenDialogFragment on LodgingPlainDialog {
	__typename
	content
	trigger {
		clientSideAnalytics {
			linkName
			referrerId
		}
		icon {
			description
			id
		}
		theme
		value
	}
	toolbar {
		title
		icon {
			description
		}
		clientSideAnalytics {
			linkName
			referrerId
		}
	}
}
fragment LodgingDialogToolbarFragment on LodgingDialogToolbar {
	icon {
		...IconFragment
	}
	title
	clientSideAnalytics {
		...ClientSideAnalyticsFragment
	}
}
fragment LodgingDialogTriggerMessageFragment on LodgingDialogTriggerMessage {
	clientSideAnalytics {
		...ClientSideAnalyticsFragment
	}
	icon {
		...IconFragment
	}
	theme
	value
	secondaryValue
}
fragment ClientSideAnalyticsFragment on ClientSideAnalytics {
	linkName
	referrerId
}
fragment MoneyFragment on Money {
	amount
	currencyInfo {
		...CurrencyFragment
	}
	formatted
}
fragment CurrencyFragment on Currency {
	code
	name
	symbol
}
fragment AlternateDateOptionFragment on AlternateDateOption {
	dates {
		link {
			uri {
				relativePath
			}
			referrerId
		}
		value
	}
	price {
		displayPrice {
			formatted
		}
	}
}
fragment TripSummaryFragment on TripSummaryContent {
	header {
		text
	}
	summary {
		value
	}
	price {
		...PriceDisplayFragment
		options {
			displayPrice {
				formatted
			}
			strikeOut {
				formatted
			}
			accessibilityLabel
			priceDisclaimer {
				content
				tertiaryUIButton {
					primary
					action {
						analytics {
							referrerId
							linkName
						}
					}
				}
				trigger {
					clientSideAnalytics {
						linkName
						referrerId
					}
					value
				}
			}
		}
		priceMessaging {
			value
		}
	}
}
fragment SingleOfferFragment on SingleUnitOfferDetails {
	availabilityCallToAction {
		__typename
		... on LodgingPlainMessage {
			value
		}
		... on LodgingButton {
			text
		}
	}
	accessibilityLabel
	displayPrice {
		leadPrice {
			...LodgingEnrichedMessageFragment
		}
		priceLabel {
			...LodgingEnrichedMessageFragment
		}
		priceMessages {
			...LodgingEnrichedMessageFragment
		}
	}
	id
	ratePlans {
		...RatePlanFragment
	}
	totalPrice {
		amount {
			...LodgingEnrichedMessageFragment
		}
		label {
			...LodgingEnrichedMessageFragment
		}
	}
}
fragment PriceDisplayFragment on PropertyPrice {
	alignment
	displayMessages {
		lineItems {
			...PriceMessageFragment
			... on LodgingEnrichedMessage {
				__typename
				value
				state
			}
		}
	}
}
fragment PriceMessageFragment on DisplayPrice {
	__typename
	role
	price {
		formatted
		accessibilityLabel
	}
	disclaimer {
		content
		primaryUIButton {
			accessibility
			primary
		}
	}
}
fragment PricePresentationDialogFragment on Offer {
	pricePresentationDialog {
		toolbar {
			title
			icon {
				description
			}
			clientSideAnalytics {
				linkName
				referrerId
			}
		}
		trigger {
			clientSideAnalytics {
				linkName
				referrerId
			}
			value
		}
	}
	pricePresentation {
		title {
			primary
		}
		sections {
			...PricePresentationSectionFragment
		}
		footer {
			header
			messages {
				...PriceLineTextFragment
				...PriceLineHeadingFragment
			}
		}
	}
}
fragment PricePresentationSectionFragment on PricePresentationSection {
	header {
		name {
			...PricePresentationLineItemEntryFragment
		}
		enrichedValue {
			...PricePresentationLineItemEntryFragment
		}
	}
	subSections {
		...PricePresentationSubSectionFragment
	}
}
fragment PriceLineTextFragment on PriceLineText {
	__typename
	theme
	primary
	weight
	additionalInfo {
		...AdditionalInformationPopoverFragment
	}
	icon {
		id
		description
		size
	}
}
fragment PriceLineHeadingFragment on PriceLineHeading {
	__typename
	primary
	tag
	size
	additionalInfo {
		...AdditionalInformationPopoverFragment
	}
	icon {
		id
		description
		size
	}
}
fragment PricePresentationLineItemEntryFragment on PricePresentationLineItemEntry {
	primaryMessage {
		...PriceLineTextFragment
		...PriceLineHeadingFragment
	}
	secondaryMessages {
		...PriceLineTextFragment
		...PriceLineHeadingFragment
	}
}
fragment PricePresentationSubSectionFragment on PricePresentationSubSection {
	header {
		name {
			primaryMessage {
				... on PriceLineText {
					primary
				}
				... on PriceLineHeading {
					primary
				}
			}
		}
		enrichedValue {
			...PricePresentationLineItemEntryFragment
		}
	}
	items {
		...PricePresentationLineItemFragment
	}
}
fragment PricePresentationLineItemFragment on PricePresentationLineItem {
	enrichedValue {
		...PricePresentationLineItemEntryFragment
	}
	name {
		...PricePresentationLineItemEntryFragment
	}
}
fragment AdditionalInformationPopoverFragment on AdditionalInformationPopover {
	icon {
		id
		description
		size
	}
	analytics {
		linkName
		referrerId
	}
	enrichedSecondaries {
		...AdditionalInformationPopoverSectionFragment
	}
}
fragment AdditionalInformationPopoverSectionFragment on AdditionalInformationPopoverSection {
	__typename
	... on AdditionalInformationPopoverTextSection {
		...AdditionalInformationPopoverTextSectionFragment
	}
	... on AdditionalInformationPopoverListSection {
		...AdditionalInformationPopoverListSectionFragment
	}
}
fragment AdditionalInformationPopoverTextSectionFragment on AdditionalInformationPopoverTextSection {
	__typename
	text {
		text
	}
}
fragment AdditionalInformationPopoverListSectionFragment on AdditionalInformationPopoverListSection {
	__typename
	content {
		__typename
		items {
			text
		}
	}
}
"""
